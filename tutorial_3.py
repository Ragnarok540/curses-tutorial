import curses
from curses import wrapper
from time import sleep


def main(stdscr):
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(2)

    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for _ in range(100):
        for j in range(26):
            c = chr(65 + j)
            pad.addstr(c, GREEN_AND_BLACK)

    # pad.refresh(0, 0, 5, 5, 25, 75)

    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        # pad.refresh(0, i, 5, 5, 10, 25)
        pad.refresh(0, 0, 5, i, 10, 25 + i)
        sleep(0.2)

    stdscr.getch()


wrapper(main)
