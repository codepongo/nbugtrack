
import os
import nbt_global
import db

# is there a better way to do these things? spaghetti code follows:

def init_db():
    ''' initialize data base here:
             basically, create tables: project, bug, wiki '''
    db.exec_cmd(nbt_global.def_dbname, nbt_global.project_table)
    db.exec_cmd(nbt_global.def_dbname, nbt_global.bugs_table)
    db.exec_cmd(nbt_global.def_dbname, nbt_global.wiki_table)

def list_projects():
    ''' if db file is not there call init_db()'''
    if not os.path.exists(nbt_global.def_dbname):
        init_db()
    else:
        proj_list = db.exec_cmd(nbt_global.def_dbname, 'select * from projects')
        return [proj_list,"projects"]

def new_project(name, desc):
    ''' add a new project to the projects table'''
    db.exec_cmd(nbt_global.def_dbname, 'insert into projects values(name,desc)')
    return list_projects()

def rename_project(id, newname):
    ''' rename the project '''
    db.exec_cmd(nbt_global.def_dbname,'update projects set shortname=? where rowid=?',(newname, id))
    return list_projects()

def update_project(id, desc):
    ''' update the project description '''
    db.exec_cmd(nbt_global.def_dbname,'update projects set description=? where rowid=?',(desc, id))
    return view_project(id=id)

def delete_project(id):
    ''' delete the project, associated wiki pages and bugs'''
    db.exec_cmd(nbt_global.def_dbname,'delete from wiki where projectid=?',(id))
    db.exec_cmd(nbt_global.def_dbname,'delete from bugs where projectid=?',(id))
    db.exec_cmd(nbt_global.def_dbname,'delete from projects where rowid=?',(id))
    return list_projects()

def view_project(project_name="",id=""):
    ''' view the project contents, bugs, wiki info.
    '''
    if project_name != "": # returns a list of [string, tuple, tuple]
        project_id = str(db.exec_cmd(nbt_global.def_dbname, 'select rowid from projects where shortname=?',(project_name,))[0][0]) # has to be a tuple
        project_description = str(db.exec_cmd(nbt_global.def_dbname, 'select description from projects where rowid=?',(project_id,))[0][0])
        return [[project_description, get_bugs(project_id), get_wiki(project_id)], "view_project"]
    elif id != "":
        project_description = str(db.exec_cmd(nbt_global.def_dbname, 'select description from projects where rowid=?',(id,))[0][0])
        return [[project_description, get_bugs(id), get_wiki(id)], "view_project"]
    else:
        nbt_global.DEBUG('view_project','either project_name or id needs to be present',err_chr='!!')
        exit()

def get_bugs(projectid):
    ''' returns the bugs associated with this project '''
    project_bugs = db.exec_cmd(nbt_global.def_dbname, 'select * from bugs where projectid=?', (projectid,))
    return [project_bugs, "bugs"] 

def get_wiki(projectid):
    ''' returns the wiki pages associated with this project '''
    project_wiki = db.exec_cmd(nbt_global.def_dbname, 'select * from wiki where projectid=?', (projectid,))
    return [project_wiki, "wiki"]

def view_bug(project_name="", id=""):
    ''' displays the bug page'''
    if not id == "":
        bug_descr = db.exec_cmd(nbt_global.def_dbname, 'select * from bugs where id=?',(id,))
        return [bug_descr, "view_bug"]
    else:
        nbt_global.DEBUG('view_bug','id needs to be present',err_chr='!!')
        exit()

def update_bug(id, params):
    ''' update the bug'''
    projectid,shortname,description,priority,status = params.split(',')
    db.exec_cmd(nbt_global.def_dbname, 'update bugs set projectid=?, shortname=?, description=?, priority=?, status=? where id=?', (projectid, shortname, description, priority, status, id,))
    return view_bug(id=id)

def delete_bug(id):
    ''' delete the bug'''
    project_id = str(db.exec_cmd(nbt_global.def_dbname, 'select projectid from wiki where rowid=?', (id,))[0][0])
    return view_project(id=projectid)

def view_wiki(project_name="", id=""):
    ''' displays the wiki page'''
    if not id == "":
        wiki_descr = db.exec_cmd(nbt_global.def_dbname, 'select * from wiki where id=?',(id,))
        return [wiki_descr, "view_wiki"]
    else:
        nbt_global.DEBUG('view_bug','id needs to be present',err_chr='!!')
        exit()

def update_wiki(id, content):
    ''' updates the wiki page'''
    db.exec_cmd(nbt_global.def_dbname, 'update wiki set content=? where id=?', (content, id,))
    return view_wiki(id=id)

def delete_wiki(id):
    ''' deletes the wiki page'''
    project_id = str(db.exec_cmd(nbt_global.def_dbname, 'select projectid from wiki where rowid=?', (id,))[0][0])
    db.exec_cmd(nbt_global.def_dbname, 'update wiki set content=? where id=?', (content, id))
    return view_project(id=projectid)

def rename_wiki(id, newname):
    ''' renames the wiki page to given name'''
    db.exec_cmd(nbt_global.def_dbname,'update wiki set shortname=? where projectid=?',(newname, id))
    return view_project(id=id)
