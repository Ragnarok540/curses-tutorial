import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    BLUE_AND_YELLOW = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(2)

    win = curses.newwin(3, 18, 2, 2)
    box = Textbox(win)
    rectangle(stdscr, 1, 1, 5, 20)
    stdscr.refresh()
    box.edit()
    text = box.gather().strip().replace('\n', '')
    stdscr.addstr(10, 40, text)
    stdscr.getch()


wrapper(main)
