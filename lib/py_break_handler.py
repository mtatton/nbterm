#
# PROGRAM: PYTHON CONSOLE DATABASE BROWSER
# MODULE : CONTROL-C HANDLER
#

import signal
import curses


def handler(signum, frame):
    # curses.echo()
    # curses.wrap()
    curses.endwin()
    print("Thank You for using this program...")
    exit()


signal.signal(signal.SIGINT, handler)
