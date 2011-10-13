
README for Version 0.1
----------------------

## PITCH: ##

Oh yeah, so yet another Bugzilla clone eh? Well, not so! 

This is:

* Simple to Use and Setup
* Includes a Wiki with Markdown formatting
* Great for Personal Projects (coz, there are no users ;)
* No Bitching in the Comments Area (coz, there are no comments ;)

## HOW TO RUN: ##

1. Extract the zip file.
2. `cd <extracted_folder>/nbugtrack`
3. `python nbugtrack.py`

## DEPS: ##

Stock python, sqlite; Markdown module for the wiki can be installed like so:

      [sudo] easy_install Markdown

If you don't install/need Markdown support, the wiki content will be interpreted as plain text. But of-course, Markdown is recommended.
   
## FUTURE PLANS: (Ordered by Priority) ##

* Add TARGET Planning (EXCEL type tables that many people love)
* MySQL / Postgres Database Support
* Configs, Preferences for categories, styles and all that jazz
* A little command line tool (nbt) to post bugs
* Authentication / Users (SSL)
* Comments, Assignees, Email Floods :-P
