
# wrapper around sqlite's data base functionality

import nbt_global
import sqlite3

def exec_cmd(dbname, cmd_string, qualifier=""):
    ''' execute the command on the database '''
    print(cmd_string)
    print(qualifier)

    try:
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        query_result = []

        if cmd_string != "":
            if qualifier == "": cur.execute(cmd_string)
            else: cur.execute(cmd_string, qualifier)

            conn.commit()
            query_result = cur.fetchall()
            cur.close()

            if query_result != None:
                return query_result
        else:
            nbt_global.DEBUG("exec_cmd: ",cmd_string,"!")
    except Exception as e:
        nbt_global.DEBUG("exec_cmd: "+str(e),cmd_string,"!")

