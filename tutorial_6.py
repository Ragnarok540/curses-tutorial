import curses
from curses import wrapper
from curses.textpad import rectangle


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    BLUE_AND_YELLOW = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(2)

    stdscr.clear()
    stdscr.border()

    stdscr.attron(GREEN_AND_BLACK)
    rectangle(stdscr, 1, 2, 5, 20)
    stdscr.attroff(GREEN_AND_BLACK)

    stdscr.move(10, 20)

    stdscr.refresh()
    stdscr.getch()


wrapper(main)
