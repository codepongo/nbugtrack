# view module: Is there is a better way to do this stuff?
# I'm thinking along the lines of seperate templates for various views
# like wiki, bug etc., But to keep it simple, the following works for now.

import nbt_global

try:
    import markdown
except ImportError as e:
    nbt_global.DEBUG(str(e), "Markdown not available, expect wiki pages to have limited appeal :P" ,"!")

view_table = {
    "projects": lambda(content): show_projects(content), # screwed up the naming
    "view_project": lambda(content): view_this_project(content),
    "bugs": lambda(content): show_bugs(content),
    "wiki": lambda(content): show_wiki(content),
    "view_bug": lambda(content): view_this_bug(content),
    "view_wiki": lambda(content): view_this_wiki(content),
}

def get_template(template=nbt_global.def_template):
    '''Gets the default HTML template; to change the appearance of the generated site, add your templates in the "templates" directory and change the def_template to that. The default template is a good place to begin.'''
    f = open("templates/"+template)
    temp_html = f.read()
    f.close()
    return temp_html

default_template = get_template()
    
def showView(data):
    ''' tuple in case of list_projects, get_bugs, get_wiki, view_bug, view_wiki
        list of 'string, tuple, tuple'in the case of view_project() '''
    result_type = data[1]
    return view_table[result_type](data[0])

def show_projects(content):
    ''' list_projects is the controller function '''
    proj_html = '''<div id="proj_data">
                   <table class="list_projects">'''
    
    for proj_data in content:
        name = str(proj_data[0])
        desc = str(proj_data[1]) # unicode to string
        
        proj_html += '''<tr><th><a href="'''+name+'''/">'''+name+'''</a></th><td>'''+desc+'''</td></tr>'''

    proj_html += '''</table></div>'''
    return default_template.replace("$page_body",proj_html).replace("$page_title","Projects")

def view_this_project(content):
    return str(content)

def show_bugs(content):
    return str(content)

def show_wiki(content):
    return str(content)

def view_this_bug(content):
    return str(content)

def view_this_wiki(content):
    return str(content)
