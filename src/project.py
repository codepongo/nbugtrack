
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
    pass

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

def view_project(project_name):
    ''' view the project contents, bugs, wiki info'''
    pass

def get_bugs():
    ''' returns the bugs associated with this project '''
    pass

def get_wiki():
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
