#
# PROGRAM: PYTHON CONSOLE DATABASE BROWSER
# MODULE : SQLITE DATABASE CONNECTOR
#

import sqlite3
import traceback
import sys

connstr = "./db/001.db"


def set_conn(p_db_name):
    global connstr
    connstr = p_db_name


def get_conn():
    global connstr
    return connstr


def qry2dict(qry, qry_params=()):
    res = {}
    try:
        con = sqlite3.connect(get_conn())
        cur = con.cursor()
        cur.execute(qry, qry_params)
        con.commit()
        data = cur.fetchall()
        if len(data) > 0:
            cols = []
            for col in cur.description:
                cols.append(col[0])
            con.close()
            i = 0
            for col in cols:
                res[col] = []
                for row in data:
                    res[col].append(row[i])
                i += 1
        return res
    except Exception:
        con.close()
        traceback.print_exc(file=sys.stdout)
        print("ERR [ FAILED QRY DATABASE ] 001000x0010 (1) : Cannot Query Database")
