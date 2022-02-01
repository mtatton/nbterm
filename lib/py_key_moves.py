#
# PROGRAM: PYTHON CONSOLE DATABASE BROWSER
# MODULE : KEY PRESS PROCESSOR
#


def key_moves(
    he,  # screen height
    k,  # pressed keycode
    curx,  # current cell x coordinate
    cury,  # current cell y coordinate
    maxx,  # number of columns
    maxy,  # number of rows
    cur_win,  # current window [ left, right ]
    tabf,  # visible rows shift from
    tabt,  # visible rows shift number
    act,  # action
    curtabsf,  # left window visible records shift
    colshift=0,  # right window columns shift
):
    act = ""
    if k == ord("j"):
        if cury < maxy:
            cury += 1
    elif k == ord("k"):
        if cury > 1:
            cury -= 1
    elif k == ord("h"):
        if curx > 0:
            curx -= 1
    elif k == ord("l"):
        if curx < maxx:
            curx += 1
    elif k == ord("L"):
        colshift += 1
    elif k == ord("H"):
        colshift -= 1
    elif k == ord("0"):
        curx = 0
    elif k == ord("G"):
        curx = maxx
        cury = maxy
    elif k == ord("n"):
        tabf += 10
    elif k == ord("u"):
        if tabf >= 10:
            tabf -= 10
    elif k == ord("s"):
        act = "asc"
    elif k == ord("S"):
        act = "desc"
    elif k == ord("f"):
        act = "filter"
    elif k == ord("\t"):
        if cur_win == "left":
            cur_win = "right"
        elif cur_win == "right":
            cur_win = "left"
    elif k == ord("m"):
        curtabsf += he - 1
    elif k == ord("i"):
        curtabsf -= he - 1
    elif k == ord("/"):
        action = "seltab"
    return (curx, cury, cur_win, tabf, tabt, act, curtabsf, colshift)
