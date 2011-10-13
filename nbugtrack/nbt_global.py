# global variables and common functions

import time

def_dbname = "nbugtrack.db"
def_template = "index.html"
def_shortchars = 50 # number of characters to display
project_table = "create table projects (shortname text unique, description text);"
bugs_table = "create table bugs (projectid integer, shortname text unique, description text, priority text, status text, foreign key(projectid) references project(rowid));" 
wiki_table = "create table wiki (projectid integer, shortname text unique, content text, foreign key(projectid) references project(rowid));"


def DEBUG(exception, info="", err_chr="D"):
    ''' prints a nice debug log '''

    print(2*err_chr),
    print(': '+exception)
    
    if info != "":
        print("\n\t"+info)
