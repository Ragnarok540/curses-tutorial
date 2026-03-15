import curses
from curses import wrapper
from curses.textpad import rectangle


def create_button(stdscr, y, x, y1, x1, text):
    rectangle(stdscr, y, x,  y + 2, x + 4)
    stdscr.refresh()
    win = curses.newwin(y1, x1, y + 1, x + 2)
    # win.clear()
    win.addstr(text)
    return win

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(1)

    stdscr.clear()

    win_1 = create_button(stdscr, 1, 1, 1, 2, '1')
    win_1.refresh()

    win_2 = create_button(stdscr, 1, 7, 1, 2, '2')
    win_2.refresh()

    win_3 = create_button(stdscr, 1, 13, 1, 2, '3')
    win_3.refresh()

    win_c = create_button(stdscr, 1, 19, 1, 2, 'C')
    win_c.refresh()

    win_4 = create_button(stdscr, 4, 1, 1, 2, '4')
    win_4.refresh()

    win_5 = create_button(stdscr, 4, 7, 1, 2, '5')
    win_5.refresh()

    win_6 = create_button(stdscr, 4, 13, 1, 2, '6')
    win_6.refresh()

    win_d = create_button(stdscr, 4, 19, 1, 2, 'D')
    win_d.refresh()

    win_7 = create_button(stdscr, 7, 1, 1, 2, '7')
    win_7.refresh()

    win_8 = create_button(stdscr, 7, 7, 1, 2, '8')
    win_8.refresh()

    win_9 = create_button(stdscr, 7, 13, 1, 2, '9')
    win_9.refresh()

    win_e = create_button(stdscr, 7, 19, 1, 2, 'E')
    win_e.refresh()

    win_a = create_button(stdscr, 10, 1, 1, 2, 'A')
    win_a.refresh()

    win_0 = create_button(stdscr, 10, 7, 1, 2, '0')
    win_0.refresh()

    win_b = create_button(stdscr, 10, 13, 1, 2, 'B')
    win_b.refresh()

    win_f = create_button(stdscr, 10, 19, 1, 2, 'F')
    win_f.refresh()

    stdscr.refresh()
    stdscr.move(20, 20)
    stdscr.getch()


wrapper(main)
