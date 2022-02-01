#
# PROGRAM: PYTHON CONSOLE DATABASE BROWSER
# MODULE : ORACLE DATABASE CONNECTOR
#

import cx_Oracle
import traceback
import sys
import os
import json

connfile = "./etc/sqlok_conn.json"

constr = None
dsn = None


def create_dns():
    global con
    global constr
    if os.path.exists(connfile):
        f = open(connfile, "r")
        dbcontmp = f.read()
        f.close()
        constr = json.loads(dbcontmp)
        # dsn = create_dns(constr)
        con = cx_Oracle.connect(
            user=constr["user"], password=constr["password"], dsn=dsn
        )


def set_conn(p_db_name):
    global connstr
    connstr = p_db_name


def get_conn():
    global connstr
    return connstr


def qry2dict(qry, qry_params=()):
    global constr
    global con
    dsn = create_dns()
    res = {}
    try:
        if con is None:
            # con = sqlite3.connect(get_conn())
            con = cx_Oracle.connect(
                user=constr["user"], password=constr["password"], dsn=dsn
            )
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
        pass
