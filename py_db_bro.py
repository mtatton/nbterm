#!/usr/bin/python3
#
# (c) MMXXII UNKNOWN
#
# PROGRAM: PYTHON CONSOLE DATABASE BROWSER
# MODULE : MAIN PROGRAM
#
# VERSION: 0.1a
#
# CHANGELOG:
#
# 20220201 BUGFIXING
# 20220131 ORA VERSION
# 20220130 INITIAL VERSION
#
# WORKDLOG:
#
# SCROLL, ORDER, FILTER
#
# BUGS:
#
# TBD:
#
# OPEN CELL VALUE IN WINDOW (FOR LONG TEXTS)
#

import curses
import traceback
import os.path
import sys

from lib.py_prn_list import prn_list
from lib.py_curses_lib import init_colors
from lib.py_key_moves import key_moves
from lib.py_error_handler import error_handler
import lib.py_break_handler

con = None

if len(sys.argv) == 1:
    DB = "ora"
else:
    DB = "lit"

if DB == "lit":
    from lib.py_sqlite_db import qry2dict
    from lib.py_sqlite_db import set_conn
elif DB == "ora":
    import lib.py_ora_db
    from lib.py_ora_db import qry2dict

sql_tab_cols = {"ora": "", "lit": ""}

# sqlite
sql_tab_cols[
    "lit"
] = """-- GET TABLE COLUMNS
select group_concat(name,'|') as cols
from pragma_table_info('%TABLE%')
order by cid asc"""

# oracle
sql_tab_cols[
    "ora"
] = """-- GET TABLE COLUMNS
select listagg(column_name,'|') as "cols"
from user_tab_columns
where table_name = '%TABLE%'
order by column_name asc"""

sql_get_tabs = {"ora": "", "lit": ""}

# sqlite
sql_get_tabs[
    "lit"
] = """-- GET TABLES
select name
from sqlite_master sm
where type in ('table','view')
order by name asc
limit ?, ?"""

# oracle
sql_get_tabs[
    "ora"
] = """-- GET TABLES
select table_name as "name"
from user_tables sm
where %FILTER%
order by table_name asc
offset :1 rows fetch 
next :2 rows only"""

sql_get_tab = {"ora": "", "lit": ""}

# sqlite
sql_get_tab[
    "lit"
] = """-- GET TABLE CONTENT
select a.rowid, a.*
from %TABLE% a
where %FILTER%
order by %SORTED%
limit ?, ?"""

# oracle
sql_get_tab[
    "ora"
] = """-- GET TABLE CONTENT
select a.rowid as "rowid", a.*
-- select 1 as "rowid", a.*
from %TABLE% a
where %FILTER%
order by %SORTED%
offset :1 rows fetch 
next :2 rows only"""


def prn_title(title):
    screen.move(he - 1, 0)
    screen.clrtoeol()
    screen.addstr(str(title), col["miGr"])


def cls():
    # screen.clear()
    screen.move(0, 0)
    cy = 0
    for cy in range(0, he):
        screen.move(cy, 0)
        screen.clrtoeol()


def read_str(p_banner):
    key = "0"
    str = ""
    screen.move(he - 1, 0)
    screen.addstr(p_banner, col["hiGr"])
    screen.move(0, 0)
    while key != 10:
        screen.clrtoeol()
        key = screen.getch()
        if (
            (key >= ord("0") and key <= ord("9"))
            or (key >= ord("A") and key <= ord("Z"))
            or (key >= ord("a") and key <= ord("z"))
            or key == ord("=")
            or key == ord(" ")
            or key == ord(">")
            or key == ord("<")
            or key == ord("_")
            or key == ord("-")
            or key == ord("%")
            or key == ord("*")
            or key == ord("!")
            or key == ord("$")
            or key == ord('"')
            or key == ord("'")
            or key == ord("(")
            or key == ord(")")
            or (key == 127 or key == 263 or key == 8)
        ):
            strlen = len(str)
            if key == 127 or key == 263 or key == 8:
                if strlen >= 0:
                    str = str[:-1]
                    strlen = len(str)
                    screen.move(0, strlen)
                    screen.delch()
            else:
                str += chr(key)
                screen.attrset(col["hiGr"])
                screen.addch(chr(key))
    return str


try:
    # PROCESS PROGRAM COMMAND LINE PARAMETER
    dbfile = ""
    if len(sys.argv) > 1:
        DB = "lit"
        dbfile = sys.argv[1]
        if not os.path.isfile(dbfile):
            print("Invalid file specified")
            exit()

    # CURSES INIT
    screen = curses.initscr()
    curses.noecho()
    col = init_colors()
    he, wi = screen.getmaxyx()

    curx = 0
    cury = 1
    maxx = 0
    maxy = 0
    k = None
    cur_win = "left"
    p_cur_win = "left"
    tabf = 0
    tabt = 0
    rcurx = 0
    rcury = 1
    rtabf = 0
    rtabt = he - 1
    rsortcol = 1
    act = ""
    sorted = 0
    sortdir = "asc"
    rfilter = "1=1"
    filtered = 0
    maxxd = 1
    maxyd = 1
    curtabsf = 0  # table list shift
    curtabst = he - 2  # table list shift sizeeee
    colshift = 0  # right table column shift
    voidcs = 0  # dummy colshift for left call
    lfiltered = 0  # table list filtered

    # MAIN INTERACTION
    while k != ord("q"):
        he, wi = screen.getmaxyx()
        p_cur_win = cur_win
        if cur_win == "left":
            curx, cury, cur_win, tabf, tabt, act, curtabsf, colshift = key_moves(
                he,
                k,
                curx,
                cury,
                maxx,
                maxy,
                cur_win,
                tabf,
                tabt,
                act,
                curtabsf,
                colshift,
            )
        else:
            rcurx, rcury, cur_win, rtabf, rtabt, act, curtabsf, colshift = key_moves(
                he,
                k,
                rcurx,
                rcury,
                maxxd,
                maxyd,
                cur_win,
                rtabf,
                rtabt,
                act,
                curtabsf,
                colshift,
            )
        if cur_win != p_cur_win:
            rcurx = 0
            rcury = 1
            rtabf = 0
            sortdir = ""
            rsortcol = 1
            rfilter = "1=1"
            colshift = 0
        if act == "filter" and cur_win == "left":
            lfilter = ""
            screen.move(0, 0)
            lfilter = read_str("Enter tables filter: lower(table) name like '%...%'")
            if lfilter == "":
                lfiltered = 0
            else:
                lfiltered = 1
                cury = 1
            act = ""
            screen.move(0, 0)
            screen.clrtoeol()
            sql_act_tabs = sql_get_tabs[DB].replace(
                "%FILTER%", "lower(table_name) like '%{}%'".format(lfilter)
            )
        elif lfiltered == 0:
            lfilter = "1=1"
            sql_act_tabs = sql_get_tabs[DB].replace("%FILTER%", "{}".format(lfilter))
        if cur_win == "left":
            cur, maxx, maxy, xcolsz = prn_list(
                DB,
                screen,
                wi,
                he,
                dbfile,
                sql_act_tabs,
                (
                    curtabsf,
                    curtabst,
                ),
                0,
                0,
                curx,
                cury,
                0,
                voidcs,
            )
        sql_cur_tab = sql_get_tab[DB].replace("%TABLE%", cur.replace("\n", ""))
        # FILTER
        cols = qry2dict(sql_tab_cols[DB].replace("%TABLE%", cur.replace("\n", "")))
        if act == "filter" and cur_win == "right":
            key = ""
            rfilter = ""
            screen.move(0, 0)
            rfilter = read_str("Enter table filter: where ... ")
            if rfilter == "":
                rfilter = "1=1"
            act = ""
            filtered = 1
            screen.move(0, 0)
            screen.clrtoeol()
        if filtered == 0:
            sql_cur_tab = sql_cur_tab.replace("%FILTER%", "1=1")
        else:
            sql_cur_tab = sql_cur_tab.replace("%FILTER%", rfilter)
        if act != "":
            rsortcol = rcurx + 2
            sql_cur_tab = sql_cur_tab.replace("%SORTED%", str(rsortcol) + " " + act)
            sorted = rsortcol
            sortdir = act
        if sorted == 0:
            sql_cur_tab = sql_cur_tab.replace("%SORTED%", "1 asc")
        if sorted != 0:
            sql_cur_tab = sql_cur_tab.replace("%SORTED%", str(rsortcol) + " " + sortdir)
        screen.move(0, wi - 1)
        sql_cur_tab = sql_cur_tab.replace("%FILTER%", rfilter)
        if sorted == 0:
            sql_cur_tab = sql_cur_tab.replace("%SORTED%", "1 asc")
        if act != "":
            rsortcol = rcurx + 2
            sql_cur_tab = sql_cur_tab.replace("%SORTED%", str(rsortcol) + " " + act)
            sorted = rsortcol
            sortdir = act
        if sorted != 0:
            sql_cur_tab = sql_cur_tab.replace("%SORTED%", str(rsortcol) + " " + sortdir)
        if cur_win == "left":
            rwinshift = sum(xcolsz) + 1
        else:
            rwinshift = 2
            screen.move(0, 0)
            screen.addstr("<", col["loGr"])
        try:
            curd, maxxd, maxyd, xcoldsz = prn_list(
                DB,
                screen,
                wi,
                he,
                dbfile,
                sql_cur_tab,
                (rtabf, rtabt),
                rwinshift,
                0,
                rcurx,
                rcury,
                1,
                colshift,
            )
        except Exception as e:
            error_handler(screen, he, e, sys.exc_info())
            screen.refresh()
            tmp = screen.getch()
        if maxyd == 0:  # NO DATA
            sql_cur_cols = sql_tab_cols[DB].replace("%TABLE%", cur.replace("\n", ""))
            curd, maxxd, maxyd, xcoldsz = prn_list(
                DB, screen, wi, he, dbfile, sql_cur_cols, (), rwinshift, 0, 0, 0, voidcs
            )
            screen.move(2, rwinshift)
            screen.addstr("--| NO DATA |--", col["miGr"])
        prn_title(
            str(rsortcol)
            + " "
            + str(rtabf)
            + " "
            + str(rtabt)
            + " "
            + cur_win
            + " "
            + dbfile
            + " "
            + cur
        )
        screen.move(0, wi - 1)
        k = screen.getch()
        he, wi = screen.getmaxyx()
        cls()
    curses.endwin()
except Exception as e:
    curses.noecho()
    curses.endwin()
    traceback.print_exc(file=sys.stdout)
    exit()
