#
# PROGRAM: PYTHON CONSOLE DATABASE BROWSER
# MODULE : CURSES COLORS
#

import curses
import locale

cols = {}


def init_colors():
    global cols
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
    cols["hiTe"] = curses.color_pair(1) | curses.A_BOLD
    cols["miTe"] = curses.color_pair(1)
    cols["loTe"] = curses.color_pair(1) | curses.A_DIM
    cols["hiRe"] = curses.color_pair(2) | curses.A_BOLD
    cols["miRe"] = curses.color_pair(2)
    cols["loRe"] = curses.color_pair(2) | curses.A_DIM
    cols["hiGr"] = curses.color_pair(3) | curses.A_BOLD
    cols["miGr"] = curses.color_pair(3)
    cols["loGr"] = curses.color_pair(3) | curses.A_DIM
    cols["hiBl"] = curses.color_pair(4) | curses.A_BOLD
    cols["miBl"] = curses.color_pair(4)
    cols["loBl"] = curses.color_pair(4) | curses.A_DIM
    cols["hiWh"] = curses.color_pair(5) | curses.A_BOLD
    cols["miWh"] = curses.color_pair(5)
    cols["loWh"] = curses.color_pair(5) | curses.A_DIM
    return cols
