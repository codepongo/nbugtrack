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

view_table = { # screwed up the naming
    "projects": lambda content: show_projects(content), 
    "view_project": lambda content: view_this_project(content),
    "bugs": lambda content: show_bugs(content),
    "wiki": lambda content: show_wiki(content),
    "view_bug": lambda content: view_this_bug(content),
    "view_wiki": lambda content: view_this_wiki(content),
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
    
    proj_html = '''<div id="proj_listing"><ol>'''
    for proj_data in content:
        name = str(proj_data[0])
        desc = str(proj_data[1]) # unicode to string
        
        proj_html += '''<li><div id="proj_data">'''
        proj_html += '''<div class="proj_name"><a href="'''+name+'''/">'''+name+'''</a></div>''' #+'''<div class="proj_desc">'''+desc+'''</div>'''
        proj_html += '''</div></li>'''
    proj_html += '''</ol></div>'''
    return default_template.replace("$page_body",proj_html).replace("$page_title","nbugtrack: Projects").replace("$page_header",'Projects <a href="#" onclick="new_project()">+</a>')

def view_this_project(content):
    ''' view the project description; bugs and wiki pages associated with it'''
    name = str(content[0])
    description = str(content[1])
    bugs_list = content[2]
    wiki_list = content[3]
    
    details_html = '''<div id="project_details_data">''' + '''<div id="project_description">''' + '<a id="update_trigger" href="#" onclick="update_project()">'+description +'</a>'+ '''</div></div>'''
    details_html += show_bugs(bugs_list[0])
    details_html += show_wiki(wiki_list[0])
    details_html += '<br /><a id="delete_trigger" href="#" onclick="delete_project()">'+'Delete this project'+'</a>' 
    return default_template.replace("$page_body",details_html).replace("$page_header",'<a href="/">Project</a>: '+'<a id="rename_trigger" href="#" onclick="rename_project()">'+name+'</a>').replace("$page_title",'Project: '+name)

def show_bugs(content):
    ''' return a bugs table: 
    '''
    bugs_html = '''<div id="bugs_data">
                   <h2>Bugs <a href="#" onclick="new_bug()">+</a></h2>
                   <table class="list_bugs">'''
    bugs_html += '''<tr><th>Bug Title</th><th>Priority</th><th>Status</th></tr>'''
    
    for bugs_data in content:
        bugid, projectid, name,bug_description,priority,status = (str(i) for i in bugs_data)
        bugs_html += '''<tr><td><a href="bug/?id='''+bugid+'''">'''+name[:nbt_global.def_shortchars]+('...' if len(name) > nbt_global.def_shortchars else '')+'''</a></td>'''+'''<td><a href="bug/?id='''+bugid+'''">'''+priority+'''</a></td>'''+'''<td><a href="bug/?id='''+bugid+'''">'''+status+'''</a></td></tr>'''
        
    bugs_html += '''</table></div>'''
    return bugs_html
    
def show_wiki(content):
    ''' return a wiki table '''
    wiki_html = '''<div id="wiki_data">
                   <h2>Wiki <a href="#" onclick="new_wiki()">+</a></h2>
                   <ul class="list_wiki">'''

    for wiki_data in content:
        wikiid, projectid, name, content = (str(i) for i in wiki_data)

        wiki_html += '''<li><a href="wiki/?id='''+wikiid+'''">'''+name[:nbt_global.def_shortchars]+('...' if len(name) > nbt_global.def_shortchars else '')+'''</a></li>'''

    wiki_html += '''</ul></div>'''
    return wiki_html

def view_this_bug(content):
    bugid, projectid, name, desc, prio, stat = [str(i) for i in content[0]]

    bug_html = '''<div id="bug_data">'''
    bug_html += '''<div id="bug_stat">Status: '''+stat+'''</div>'''
    bug_html += '''<div id="bug_prio">Priority: '''+prio+'''</div>'''
    
    if markdown_available == True:
        bug_html += '''<br />Description: <div id="bug_desc">'''+str(markdown.markdown(desc))+'''</div>'''
    else:
        bug_html += '''<br />Description: <div id="bug_desc"><pre>'''+str(desc)+'''</pre></div>'''

    bug_html += '<br /><a id="delete_trigger" href="#" onclick="delete_bug()">'+'Delete this bug'+'</a>' 
    bug_html += "</div>"

    return default_template.replace("$page_body",bug_html).replace("$page_header",'<a href="../">Bug</a>: <a href="#" onclick="update_bug()">'+name+'</a> (<span id="bugid">'+bugid+"</span>)").replace('$page_title',"Bug: "+name)

def view_this_wiki(content):
    pageid, projectid, pagename, pagecontent = [str(i) for i in content[0]]

    page_html = '''<div id="wiki_page">'''

    page_html += '<br /><a id="update_trigger" href="#" onclick="update_wiki()">'+'Edit this wiki'+'</a>' 

    if markdown_available == True:
        page_html += '''<div id="wiki_content">'''+str(markdown.markdown(pagecontent))+'''</div>'''
    else:
        page_html += '''<div id="wiki_content"><pre>'''+str(pagecontent)+'''</pre></div>'''
    page_html += '<br /><a id="delete_trigger" href="#" onclick="delete_wiki()">'+'Delete this wiki'+'</a>' 
    page_html += '''</div>'''

    return default_template.replace("$page_body",page_html).replace("$page_header",'<a href="../">Wiki</a>: <a id="rename_trigger" href="#" onclick="rename_wiki()">'+pagename+'</a> (<span id="pageid">'+pageid+"</span>)").replace("$page_title","Wiki: "+pagename)

