
README for Version 0.1
----------------------

## PR: ##

Oh yeah, so yet another Bugzilla clone eh? Well, not so! 

This is:

* Simple to Use
* Simple to Setup
* Includes a Wiki
* Great for Personal Projects (coz, there are no users ;)
* No Bitching in the Comments Area (coz, there are no comments ;)
   

## DB DESIGN: ##

	A simple sqlite3 database with the following tables:
	  
	BUGS:

		id integer primary key autoincrement, projectid integer, shortname text, description text, priority text, status text, foreign key(projectid) references project(id)

	WIKI:
	
		id integer primary key, projectid integer, shortname text, content text, forieign key(projectid) references project(id) 

	PROJECT:

		id integer primary key, shortname text unique, description text


## URL SPEC: ##
       /
       [ list Projects, create new project, rename project]

       /new_project?name=<Project Name> 		
       /rename_project?name=<Old Name>&newname=<New Name>
       /delete_project?name=<Project Name>

       [ view bugs/wiki, delete the project] 
       /<Project Name>/				

       [ view bug report, change status, delete bug]
       /<Project Name>/bug/?id=<bug_id> 	
       /delete_bug?pid=<project_id>&id=<bug_id>	
       /update_bug?pid=<project_id>&id=<bug_id>   

       [ view wiki page, edit, delete page]
       /<Project Name>/wiki/?id=<wiki_id> 	       
       /delete_wiki?pid=<project_id>&id=<wiki_id>	
       /update_wiki?pid=<project_id>&id=<wiki_id>   


## APP DESIGN: ##

* router.py	-> Route Requests to functions
* db.py	  	-> All database handling code, should be able to
        	   swap databases without changing anything else
* project.py	-> Model logic
* nbugtrack.py	-> Main module	
* view.py	-> Display logic

## FUTURE PLANS: (Ordered by Priority) ##

* Add TARGET Planning (EXCEL type tables that many people love)
* MySQL / Postgres Database Support
* Configs, Preferences for categories, styles and all that jazz
* A little command line tool (nbt) to post bugs
* Authentication / Users (SSL)
* Comments, Assignees, Email Floods :-P
