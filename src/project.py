
import os
import nbt_global
import db

def init_db():
    ''' initialize data base here:
             basically, create tables: project, bug, wiki '''
    db.exec_cmd(nbt_global.def_dbname, nbt_global.project_table)
    db.exec_cmd(nbt_global.def_dbname, nbt_global.bugs_table)
    db.exec_cmd(nbt_global.def_dbname, nbt_global.wiki_table)

def list_projects():
    ''' if projects table not there, database is corrupt,
        hence call init_db()'''
    if not os.path.exists(nbt_global.def_dbname):
        init_db()
    else:
        proj_list = db.exec_query(nbt_global.def_dbname, 'select * from projects')
        return str(proj_list)

def new_project(name):
    ''' add a new project to the projects table'''
    pass

def rename_project(id, newname):
    ''' rename the project '''
    pass

def update_project(id, desc):
    ''' update the project description '''
    pass

def delete_project(id):
    ''' delete the project, associated wiki pages and bugs'''
    pass

# XXX: THIS IS A WHOLE FUCKING SOUP OF SPAGHETTI
def view_project(project_name):
    ''' view the project contents, bugs, wiki info'''
    project_id = str(db.exec_query(nbt_global.def_dbname, 'select rowid from projects where shortname=?',(project_name,))[0][0]) # has to be a tuple
    project_description = str(db.exec_query(nbt_global.def_dbname, 'select description from projects where rowid=?',(project_id,))[0][0])
    return project_description 

def get_bugs(projectid):
    ''' returns the bugs associated with this project '''
    pass

def get_wiki(projectid):
    ''' returns the wiki pages associated with this project '''
    pass

def view_bug(project_name, id):
    ''' displays the bug page'''
    pass

def update_bug(id, params):
    ''' update the bug'''
    pass

def delete_bug(id):
    ''' delete the bug'''
    pass

def view_wiki(project_name, id):
    ''' displays the wiki page'''
    pass

def delete_wiki(id):
    ''' deletes the wiki page'''
    pass

def update_wiki(id, content):
    ''' updates the wiki page'''
    pass

def rename_wiki(id, newname):
    ''' renames the wiki page to given name'''
    pass
