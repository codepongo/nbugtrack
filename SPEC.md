
## DB DESIGN: ##

A simple sqlite3 database with the following tables:

0. PROJECT:

		`shortname text unique, description text`
	  
1. BUGS:

		`projectid integer, shortname text, description text, priority text, status text, foreign key(projectid) references project(rowid)`

2. WIKI:
	
		`projectid integer, shortname text, content text, forieign key(projectid) references project(rowid)`

## URL SPEC: ##
* __list/create/rename projects__

`/`
`/new_project?name=<Project Name>`
`/rename_project?name=<Old Name>&newname=<New Name>`

* __view/delete project__
`/<Project Name>/`
`/delete_project?name=<Project Name>`
				
* __view bug report, change status, delete bug__
`/<Project Name>/bug/?id=<bug_id>` 
`/delete_bug?pid=<project_id>&id=<bug_id>`
`/update_bug?pid=<project_id>&id=<bug_id>`

* __view wiki page, edit, delete page__
`/<Project Name>/wiki/?id=<wiki_id>`
`/delete_wiki?pid=<project_id>&id=<wiki_id>`
`/update_wiki?pid=<project_id>&id=<wiki_id>`

## APP DESIGN: ##

* router.py	-> Route Requests to functions
* db.py	  	-> All database handling code, should be able to
        	   swap databases without changing anything else
* project.py	-> Model logic
* nbugtrack.py	-> Main module	
* view.py	-> Display logic
