import curses
from curses import wrapper
from time import sleep


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    BLUE_AND_YELLOW = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(2)

    counter_win = curses.newwin(1, 20, 10, 10)
    stdscr.addstr('hello world')
    stdscr.refresh()

    for i in range(20):
        counter_win.clear()
        color = BLUE_AND_YELLOW

        if i % 2 == 0:
            color = GREEN_AND_BLACK

        counter_win.addstr(f'counter {i}', color)
        counter_win.refresh()

        sleep(0.3)

    stdscr.getch()


wrapper(main)
