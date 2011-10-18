# a table of url/function pairs to route requests

import re
import project
from nbt_global import DEBUG

# Some people, when confronted with a problem, think "I know, I'll use regular 
# expressions." Now they have two problems.  --jwz (http://www.jwz.org/hacks/gdb-highlight.el)
rtable = {
    '\/*$': 'list_projects',
    '\/([\w\s\.%]+)\/*$': 'view_project',
    '\/([\w\s%]+)\/+bug\/*\?id=(\w+)$': 'view_bug',
    '\/([\w\s%]+)\/+wiki\/*\?id=(\w+)$': 'view_wiki',
    '\/delete_project\/*\?name=([\w\s\.%]+)$': 'delete_project',
    '\/delete_bug\/*\?id=(\w+)$': 'delete_bug',
    '\/delete_wiki\/*\?id=(\w+)$': 'delete_wiki',
    '\/send_wtext\/*\?id=(\w+)$': 'send_wtext',
#   '\/new_project\/*\?name=([\w\s%]+)&desc=([\w\s%]+)$': 'new_project',
#   '\/rename_project\/*\?id=(\w+)&newname=([\w\s%]+)$': 'rename_project',
#   '\/rename_wiki\/*\?id=(\w+)&name=([\w\s%]+)$': 'rename_wiki',
#    '\/update_project\/*\?id=(\w+)&desc=([\w\s%]+)$': 'update_project',
#    '\/update_bug\/*\?id=(\w+)&params=([\w\s,%]+)$': 'update_bug',
#    '\/update_wiki\/*\?id=(\w+)&content=([\w\s%]+)$': 'update_wiki', 

######## any js,css,img resource files ##########
    '\/*js\/*([\w\-\.]+)$': 'send_file',
    '\/*css\/*([\w\-\.]+)$': 'send_file',
    '\/*img\/*([\w\-\.]+)$': 'send_file',
    '\/*favicon.ico$': 'send_file'
} # updates are done with POST

# re.compile(lvalue).match(query) -> eval(rvalue)
def match(query):
    ''' matches the pattern with the respective function'''

    for pattern in rtable:
        exists = re.compile(pattern).match(query)

        if exists != None:
            exec_string = rtable[pattern]+'('+', '.join('\"'+i+'\"' for i in list(exists.groups()))+')'
            DEBUG(exec_string,err_chr='E')
            return eval('project.'+exec_string)
        
