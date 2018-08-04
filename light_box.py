#!/usr/bin/env python
from helpers.Board import Board
from curses import wrapper
import time
import random


def main(stdscr):
    board = Board()

    # This raises ZeroDivisionError when i == 10.
    # for i in range(0, 10):
    #     v = i-10
    #     stdscr.addstr(i, 10, '10 divided by {} is {}'.format(v, 10/v))

    while not board.is_game_over():
        # Clear screen
        stdscr.clear()
        random.choice(board.buttons).press()
        board.draw_curses(stdscr)
        time.sleep(.05)
        stdscr.refresh()
    stdscr.getkey()


wrapper(main)
