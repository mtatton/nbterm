#
# PROGRAM: PYTHON CONSOLE DATABASE BROWSER
# MODULE : PRINT LIST
#

from lib.py_list_to_str import list_to_str
from lib.py_get_list_vals import get_list_vals
from lib.py_curses_lib import init_colors


def prn_list(
    DB,
    screen,
    wi,
    he,
    dbfile,
    sql,
    params,
    begx=0,
    begy=0,
    curx=0,
    cury=0,
    skip_rowid=0,
    colshift=0,
):
    if DB == "lit":
        from lib.py_sqlite_db import set_conn
        from lib.py_sqlite_db import qry2dict

        set_conn(dbfile)
    elif DB == "ora":
        from lib.py_ora_db import qry2dict
    def_col_sz = 3
    col = init_colors()
    xcolsz = []
    res = qry2dict(sql, params)
    prn = list_to_str(res)
    rows = prn.split("\n")
    list_keys = list(res.keys())
    maxx = len(list_keys) - 1
    maxy = len(rows) - 1
    for i in list_keys:
        inlist = get_list_vals(res[i])
        if len(inlist) > 0:
            xlenstr = max(inlist)
        else:
            xlenstr = def_col_sz
        xcolsz.append(xlenstr)
    ret = ""
    prnx = 0
    prny = 0
    sy = begy
    curcol = 0
    for r in rows:
        curcol = 0
        sx = begx
        prnx = 0
        skipcols = colshift
        for c in r.split("|"):
            if skip_rowid == 1 and curcol == 0:
                curcol = 1
            elif skipcols > 0:
                skipcols -= 1
            else:
                strcut = wi - 1
                if sx + len(str(c)) > wi - 1:
                    strcut = wi - 1 - sx
                if sy + len(c.split("\n")) > he or strcut < 0:
                    break
                screen.move(sy, sx)
                clr = col["loGr"]
                if curx == prnx and cury == prny:
                    clr = col["hiGr"]
                    ret = c
                screen.addstr(str(c)[0:strcut], clr)
                if len(xcolsz) > 0:
                    sx += xcolsz[curcol] + 1
                prnx += 1
                curcol += 1
        if sy > he - 1:
            break
        screen.move(sy, 0)
        sy += 1
        prny += 1
    return (ret, maxx, maxy, xcolsz)
