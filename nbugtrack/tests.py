# a db connection tester

import sys
import os
import db
import nbt_global

dbname = "test.db"

def test_db():

    if not os.path.exists(dbname):        
        db.exec_cmd(dbname, nbt_global.project_table)
        db.exec_cmd(dbname, nbt_global.bugs_table)
        db.exec_cmd(dbname, nbt_global.wiki_table)
    
        # projects
        db.exec_cmd(dbname, 'insert into projects values("Example1","This is an Example project 1");')
        db.exec_cmd(dbname, 'insert into projects values("Example2","This is an Example project 1");')
        db.exec_cmd(dbname, 'insert into projects values("Example3","This is an Example project 1");')
        db.exec_cmd(dbname, 'insert into projects values("Example4","This is an Example project 1");')
        db.exec_cmd(dbname, 'insert into projects values("Example5","This is an Example project 1");')
        
        # bugs
        db.exec_cmd(dbname, 'insert into bugs values((select rowid from projects where shortname="Example1"), "Your leg is broken", "The leg is broken for the following component", "CRITICAL", "OPEN");')
        db.exec_cmd(dbname, 'insert into bugs values((select rowid from projects where shortname="Example2"), "My leg is broken", "The leg is broken for the following component", "CRITICAL", "OPEN");')
        db.exec_cmd(dbname, 'insert into bugs values((select rowid from projects where shortname="Example3"), "Our leg is broken", "The leg is broken for the following component", "CRITICAL", "OPEN");')
        db.exec_cmd(dbname, 'insert into bugs values((select rowid from projects where shortname="Example4"), "His leg is broken", "The leg is broken for the following component", "CRITICAL", "OPEN");')
        db.exec_cmd(dbname, 'insert into bugs values((select rowid from projects where shortname="Example5"), "Her leg is broken", "The leg is broken for the following component", "CRITICAL", "OPEN");')

        # wiki
        db.exec_cmd(dbname, 'insert into wiki values((select rowid from projects where shortname="Example1"), "Example Wiki Page 1", "This is a wiki page");')
        db.exec_cmd(dbname, 'insert into wiki values((select rowid from projects where shortname="Example3"), "Example Wiki Page 2", "This is a wiki page");')
        db.exec_cmd(dbname, 'insert into wiki values((select rowid from projects where shortname="Example2"), "Example Wiki Page 3", "This is a wiki page");')
        db.exec_cmd(dbname, 'insert into wiki values((select rowid from projects where shortname="Example5"), "Example Wiki Page 4", "This is a wiki page");')
        db.exec_cmd(dbname, 'insert into wiki values((select rowid from projects where shortname="Example4"), "Example Wiki Page 5", "This is a wiki page");')


    print(db.exec_query(dbname, 'select * from projects;'))

    print(db.exec_query(dbname, 'select * from bugs where projectid = (select rowid from projects where shortname = "Example3");'))
    print(db.exec_query(dbname, 'select * from bugs where projectid = (select rowid from projects where shortname = "Example5");'))
    print(db.exec_query(dbname, 'select * from bugs where projectid = (select rowid from projects where shortname = "Example1");'))
    print(db.exec_query(dbname, 'select * from bugs where projectid = (select rowid from projects where shortname = "Example2");'))
    print(db.exec_query(dbname, 'select * from bugs where projectid = (select rowid from projects where shortname = "Example4");'))
    
    print(db.exec_query(dbname, 'select * from wiki where projectid = (select rowid from projects where shortname = "Example3");'))
    print(db.exec_query(dbname, 'select * from wiki where projectid = (select rowid from projects where shortname = "Example5");'))
    print(db.exec_query(dbname, 'select * from wiki where projectid = (select rowid from projects where shortname = "Example1");'))
    print(db.exec_query(dbname, 'select * from wiki where projectid = (select rowid from projects where shortname = "Example2");'))
    print(db.exec_query(dbname, 'select * from wiki where projectid = (select rowid from projects where shortname = "Example4");'))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        dbname = sys.argv[1]
    test_db()

