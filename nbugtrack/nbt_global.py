# global variables and common functions

import time
import sys

def_dbname = "nbugtrack.db"
def_template = "index.html"
def_shortchars = 50 # number of characters to display
project_table = "create table projects (shortname text unique, description text);"
bugs_table = "create table bugs (projectid integer, shortname text, description text, priority text, status text, foreign key(projectid) references project(rowid));" 
wiki_table = "create table wiki (projectid integer, shortname text, content text, foreign key(projectid) references project(rowid));"
python_version = sys.version[:1]

def unicode_32(req_str):
    ''' smooth over unicode changes between python versions '''
    try:
        ret_str =  str(req_str, 'utf-8') if python_version == '3' else unicode(req_str)
        return ret_str
    except TypeError:
        return str(req_str)

def DEBUG(exception, info="", err_chr="D"):
    ''' prints a nice debug log '''

    print(2*err_chr+': '+exception)
    
    if info != "":
        print("\n\t"+info)
