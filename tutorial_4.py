import curses
from curses import wrapper
from curses.textpad import rectangle


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
    BLUE_AND_YELLOW = curses.color_pair(1)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(2)
    stdscr.nodelay(True)

    x, y = 5, 5

    while True:
        try:
            key = stdscr.getkey()
        except Exception:
            key = None

        match key:
            case 'KEY_LEFT':
                x -= 1
            case 'KEY_RIGHT':
                x += 1
            case 'KEY_UP':
                y -= 1
            case 'KEY_DOWN':
                y += 1

        stdscr.clear()
        # rectangle(stdscr, y, x, 10 + y, 20 + x)
        stdscr.addstr(y, x, '0')
        stdscr.refresh()
        # stdscr.getch()


wrapper(main)
