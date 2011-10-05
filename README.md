
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

		projectid integer, shortname text, description text, priority text, status text, foreign key(projectid) references project(id)

	WIKI:
	
		projectid integer, shortname text, content text, forieign key(projectid) references project(id) 

	PROJECT:

		shortname text unique, description text


## URL SPEC: ##
* __/__ : list Projects, create new project, rename project
  __/new_project?name=<Project Name>__ 		
  __/rename_project?name=<Old Name>&newname=<New Name>__
  __/delete_project?name=<Project Name>__

* __/<Project Name>/__ : view bugs/wiki, delete the project
				
* __/<Project Name>/bug/?id=<bug_id>__ : view bug report, change status, delete bug
__/delete_bug?pid=<project_id>&id=<bug_id>__	
__/update_bug?pid=<project_id>&id=<bug_id>__   

* __/<Project Name>/wiki/?id=<wiki_id>__ : view wiki page, edit, delete page
__/delete_wiki?pid=<project_id>&id=<wiki_id>__ 	
__/update_wiki?pid=<project_id>&id=<wiki_id>__   


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
