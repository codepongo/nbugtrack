
README for Version 0.1
----------------------

## PITCH: ##

Oh yeah, so yet another Bugzilla clone eh? Well, not so! 

This is:

* Simple to Use and Setup
* Includes a Wiki
* Great for Personal Projects (coz, there are no users ;)
* No bitching in the Comments Area (coz, there are no comments ;)

## HOW TO RUN: ##

1. Download and Extract the zip file.
2. `cd <extracted_folder>/nbugtrack`
3. `python nbugtrack.py`
4. Open the URL in your browser.

## DEPS: ##

Stock python (tested with CPython 2.7.1, 3.2.1, PyPy 1.6.0; YMMV with other versions), sqlite3; Markdown module for the wiki can be installed like so:

      [sudo] easy_install Markdown

If you don't install/need Markdown support, the wiki content will be interpreted as plain text. But of-course, Markdown is recommended.

## Browser Support: ##

Tested with:

* IE 8+ (Some view related bugs in IE 6/7)
* Opera (11.51) 
* Safari (5)
* jQuery callback related bugs in Firefox, Chrome
   
## FUTURE PLANS: (Ordered by Priority) ##

* Add TARGET Planning (EXCEL type tables that many people love)
* MySQL / Postgres Database Support
* Authentication / Users (SSL)
* Comments, Assignees, Duplicate Bugs, Email Floods :-P
* Scalable web servers: nginx, mongrell2, ...
* Configs, Preferences for categories, styles and all that jazz
* A little command line tool (nbt) to post bugs

