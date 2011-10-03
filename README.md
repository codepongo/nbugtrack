
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

		id(pkey), projectid, shortname, description, priority, status

	WIKI:
	
		id(pkey), projectid, shortname, content 

	PROJECT:

		id(pkey), shortname, description


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
* Configs, Preferences for categories, styles and all that jazz
* A little command line tool (nbt) to post bugs
* Authentication Token (SSL??)
* Users, Comments, Assignees, Email Floods :-P
