# global variables and common functions

import time

def_dbname = "nbugtrack.db"
project_table = "create table projects (shortname text unique, description text);"
bugs_table = "create table bugs (projectid integer, shortname text unique, description text, priority text, status text, foreign key(projectid) references project(rowid));" 
wiki_table = "create table wiki (projectid integer, shortname text unique, content text, foreign key(projectid) references project(rowid));"


def DEBUG(exception, info, err_chr="*"):
    print(10*err_chr)
    print(exception+":\n"+info)
    print(100*err_chr)
