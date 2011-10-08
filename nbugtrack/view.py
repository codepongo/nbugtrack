
def get_template(template="default.html"):
    '''Gets the default HTML template; to change the appearance of the generated site, add your templates in the templates directory and change the name to that. The default template is a good place to begin.'''
    f = open("templates/"+template)
    tem_html = f.read()
    f.close()
    return tem_html
    
def showView(data):
    ''' 
    Does a type dispatch to print the data out; returns the HTML

    tuple in case of list_projects, get_bugs, get_wiki, view_bug, view_wiki
    list of 'string, tuple, tuple'in the case of view_project()

    '''
    
    
