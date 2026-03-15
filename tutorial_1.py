import curses
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    BLUE_AND_YELLOW = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(2)
    stdscr.clear()
    stdscr.addstr(0, 0, 'hello world')
    stdscr.addstr(2, 0, 'hello world', curses.A_BOLD)
    stdscr.addstr(4, 0, 'hello world', curses.A_STANDOUT)
    stdscr.addstr(6, 0, 'hello world', curses.A_UNDERLINE)
    stdscr.addstr(8, 0, 'hello world', curses.A_DIM)
    stdscr.addstr(10, 0, 'hello world', BLUE_AND_YELLOW)
    stdscr.addstr(12, 0, 'hello world', GREEN_AND_BLACK)
    stdscr.addstr(14, 0, 'hello world', GREEN_AND_BLACK | curses.A_BOLD)
    stdscr.addstr(16, 0, 'hello world', BLUE_AND_YELLOW | curses.A_REVERSE)
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
