#!/usr/bin/env python
from helpers.Board import Board
from curses import wrapper
import random
import time


def main(stdscr):
    print("hello")
    while True:
        board = Board()
        while not board.is_game_over():
            # Clear screen
            draw_frame(stdscr, board)
            choice = stdscr.getkey()
            board.press(choice.capitalize())
            stdscr.refresh()
            time.sleep(.1)

        draw_frame(stdscr, board)
        stdscr.refresh()
        time.sleep(1.5)

        board.turn_off_all_lights()

        num_flashes = 10
        for i in range(num_flashes):
            board.toggle_all_lights()
            draw_frame(stdscr, board)
            stdscr.refresh()
            time.sleep(.5)
        time.sleep(3)


def draw_frame(stdscr, board):
    stdscr.clear()
    board.draw_curses(stdscr)


wrapper(main)
