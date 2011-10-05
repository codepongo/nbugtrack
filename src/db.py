
# these functions provide wrappers around
# sqlite's data base functionality

import nbt_global
import sqlite3

def exec_cmd(dbname, cmd_string):
    ''' execute the command on the database '''
    try:
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()

        if cmd_string != "":
            cur.execute(cmd_string)
        else:
            nbt_global.DEBUG("exec_cmd: ",cmd_string,"!")
            exit()
        conn.commit()
        cur.close()
    except sqlite3.OperationalError as e:
        nbt_global.DEBUG("exec_cmd: "+str(e),cmd_string,"!")
        exit()

def exec_query(dbname, query_string, qualifier=""):
    ''' execute the query on the database and return a list of matching rows'''
    try:
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        query_result = []

        if query_string != "":
            if qualifier=="": cur.execute(query_string)
            else: cur.execute(query_string, qualifier)
            conn.commit()
            query_result = cur.fetchall()
            cur.close()
            return query_result
        else:
            nbt_global.DEBUG("exec_cmd: ",query_string,"!")
            exit()
    except sqlite3.OperationalError as e:
        nbt_global.DEBUG("exec_cmd: "+str(e),query_string,"!")
        
