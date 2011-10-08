
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
* view_project	-> `[[project_description, get_bugs, get_wiki], "view_project"]`
* get_bugs	-> `[project_bugs, "bugs"]`
* get_wiki	-> `[project_wiki, "wiki"]`
* view_bug	-> `[bug_descr, "view_bug"]`
* view_wiki	-> `[wiki_descr, "view_wiki"]`

