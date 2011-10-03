
README for Version 0.1
----------------------

## PR: ##

	Oh yeah, so yet another Bugzilla clone eh? Well, not so! This is:

   	1) Simple to Use
   	2) Simple to Setup
   	3) Great for Personal Projects
   	4) No Bitching in the Comments Area (coz, there are no comments ;)
   

## DESIGN: ##

	A simple sqlite3 database with the following tables:
	  
	  BUGS:

		id(pkey), projectid, shortname, description, priority, status

	  WIKI:
	
		id(pkey), projectid, shortname, content 

	  PROJECT:

		id(pkey), shortname, description

