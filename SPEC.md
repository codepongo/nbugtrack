
## DB DESIGN: ##

A simple sqlite3 database with the following tables:

0. PROJECT:

		`shortname text unique, description text`
	  
1. BUGS:

		`projectid integer, shortname text, description text, priority text, status text, foreign key(projectid) references project(rowid)`

2. WIKI:
	
		`projectid integer, shortname text, content text, forieign key(projectid) references project(rowid)`

## APP DESIGN: ##

* router.py	-> Route Requests to functions
* db.py	  	-> Database querying code
* nbugtrack.py	-> Main module (controller)
* project.py	-> Model logic
* view.py	-> Display logic

## VIEW DESIGN: ##

* list_projects	-> `[proj_list, "projects"]`

 		   `[(u'Example3', u'This is an Example project 1'), (u'Example4', u'Changed Again'), (u'This is an Example Project', u'This is an Example project 1')]`

* view_project	-> `[[project_name, project_description, get_bugs, get_wiki], "view_project"]`

  		   `['Example 1','This is an Example project 1', get_bugs, get_wiki]`

* get_bugs	-> `[project_bugs, "bugs"]`

  		   `[(2, u'My leg is broken', u'The leg is broken for the following component', u'CRITICAL', u'OPEN')]`
  		   
* get_wiki	-> `[project_wiki, "wiki"]`

  		   `[(2, u'Example Wiki Page 32', u'This is a wiki page')]`

* view_bug	-> `[bug_descr, "view_bug"]`

  		   `[(2, u'My leg is broken', u'The leg is broken for the following component', u'CRITICAL', u'OPEN')]`

* view_wiki	-> `[wiki_descr, "view_wiki"]`

  		   `[(2, u'Example Wiki Page 32', u'This is a wiki page')]`
