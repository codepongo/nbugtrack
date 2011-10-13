# view module: Is there is a better way to do this stuff?
# I'm thinking along the lines of seperate templates for various views
# like wiki, bug etc., But to keep it simple, the following works for now.

import nbt_global

try:
    import markdown
    markdown_available = True
except ImportError as e:
    nbt_global.DEBUG(str(e), "Markdown not available, expect wiki pages to have limited appeal :P" ,"!")
    markdown_available = False

view_table = {
    "projects": lambda(content): show_projects(content), # screwed up the naming
    "view_project": lambda(content): view_this_project(content),
    "bugs": lambda(content): show_bugs(content),
    "wiki": lambda(content): show_wiki(content),
    "view_bug": lambda(content): view_this_bug(content),
    "view_wiki": lambda(content): view_this_wiki(content),
}

def get_template(template=nbt_global.def_template):
    '''Gets the default HTML template; to change the appearance of the generated site, add your templates in the "templates" directory and change the def_template to that. The default `index.html` template is a good place to begin.'''
    f = open("templates/"+template)
    temp_html = f.read()
    f.close()
    return temp_html

default_template = get_template()
    
def showView(data):
    ''' tuple in case of list_projects, get_bugs, get_wiki, view_bug, view_wiki
        list of 'string, tuple, tuple'in the case of view_project() '''
    result_type = data[1]

    try:
        response = view_table[result_type](data[0])
        return response
    except KeyError:
        return data
    
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
    ''' view the project description; bugs and wiki pages associated with it'''
    name = str(content[0])
    description = str(content[1])
    bugs_list = content[2]
    wiki_list = content[3]
    
    details_html = '''<div id="project_details_data">
                      <div id="project_name">
                      ''' + name + '''
                      <div id="project_description">
                      ''' + description + '''</div>'''
    details_html += show_bugs(bugs_list[0])
    details_html += show_wiki(wiki_list[0])

    return default_template.replace("$page_body",details_html).replace("$page_title","Project: "+name)

def show_bugs(content):
    ''' return a bugs table '''
    bugs_html = '''<div id="bugs_data">
                   <table class="list_bugs">'''
    bugs_html += '''<tr><th>Id</th><th>Short Name</th><th>Description</th><th>Priority</th><th>Status</th></tr>'''
    print(content)
    
    for bugs_data in content:
        bugid,name,bug_description,priority,status = (str(i) for i in bugs_data)
        bugs_html += '''<tr><td><a href="bug/?id='''+bugid+'''">'''+bugid+'''</a></td>'''+'''<td><a href="bug/?id='''+bugid+'''">'''+name[:nbt_global.def_shortchars]+('...' if len(name) > nbt_global.def_shortchars else '')+'''</a></td>'''+'''<td><a href="bug/?id='''+bugid+'''">'''+priority+'''</a></td>'''+'''<td><a href="bug/?id='''+bugid+'''">'''+status+'''</a></td></tr>'''
        
    bugs_html += '''</table></div>'''
    return bugs_html
    
def show_wiki(content):
    ''' return a wiki table '''
    wiki_html = '''<div id="wiki_data">
                   <table class="list_wiki">'''
    wiki_html += '''<tr><th>Page Id</th><th>Page Name</th></tr>'''

    for wiki_data in content:
        wikiid,name,content = (str(i) for i in wiki_data)

        wiki_html += '''<tr><td><a href="wiki/?id='''+wikiid+'''">'''+wikiid+'''</a></td>'''+'''<td><a href="wiki/?id='''+wikiid+'''">'''+name[:nbt_global.def_shortchars]+('...' if len(name) > nbt_global.def_shortchars else '')+'''</a></td></tr>'''

    wiki_html += '''</table></div>'''
    return wiki_html

def view_this_bug(content):
    bugid, name, desc, prio, stat = [str(i) for i in content[0]]

    bug_html = '''<div id="bug_data"><div id="bug_title">'''+bugid+''': '''+name+'''</div>'''
    bug_html += '''<div id="bug_stat">'''+stat+'''</div>'''
    bug_html += '''<div id="bug_prio">'''+prio+'''</div>'''

    if markdown_available == True:
        bug_html += '''<div id="bug_desc">'''+str(markdown.markdown(desc))+'''</div>'''
    else:
        bug_html += '''<div id="bug_desc">'''+str(desc)+'''</div>'''
    bug_html += '''</div>'''

    return default_template.replace("$page_body",bug_html).replace("$page_title","Bug: "+bugid)

def view_this_wiki(content):
    pageid,pagename,pagecontent = [str(i) for i in content[0]]

    page_html = '''<div id="wiki_page"><div id="wiki_title">'''+pageid+''': '''+pagename+'''</div>'''

    if markdown_available == True:
        page_html += '''<div id="wiki_content">'''+str(markdown.markdown(pagecontent))+'''</div>'''
    else:
        page_html += '''<div id="wiki_content">'''+str(pagecontent)+'''</div>'''
    page_html += '''</div>'''

    return default_template.replace("$page_body",page_html).replace("$page_title","Wiki: "+pagename)

