
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
* db.py	  	-> All database handling code, should be able to
        	   swap databases without changing anything else
* project.py	-> Model logic
* nbugtrack.py	-> Main module	
* view.py	-> Display logic
