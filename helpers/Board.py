from helpers.Light import Light
from helpers.Button import Button
from helpers.common import *
import random
import time


class Board(object):
    """

    """
    left_offset = 4
    top_offset = 1

    def __init__(self, light_rows=5, light_cols=5, num_buttons=8):
        self.light_rows = light_rows
        self.light_cols = light_cols
        self.num_buttons = num_buttons
        self.lights = []
        self.buttons = []
        self.buttons_dict = {}
        self.board = []
        self.validate()
        self.make_board()
        self.mix_board()

    def validate(self):
        assert(isinstance(self.light_rows, int))
        assert(self.light_rows > 0)
        assert(isinstance(self.light_cols, int))
        assert(self.light_cols > 0)
        assert(isinstance(self.num_buttons, int))
        assert(self.num_buttons <= 26)
        assert(self.num_buttons > 0)
        assert(self.num_buttons < (self.light_rows * self.light_cols))

    def make_board(self):
        self.make_lights()
        self.make_buttons()

    def make_lights(self):
        for row_num in range(self.light_rows):
            row = []
            for col_num in range(self.light_cols):
                light = Light()
                self.lights.append(light)
                row.append(light)
            self.board.append(row)

    def make_buttons(self):
        starting_identifier = ord("A")
        shuffled_lights = divide_with_overlap(self.lights, self.num_buttons)
        for button_num in range(self.num_buttons):
            identifier = chr(starting_identifier + button_num)
            lights = shuffled_lights[button_num]
            button = Button(identifier, lights)
            self.buttons.append(button)
            self.buttons_dict[identifier] = button

    def mix_board(self):
        shuffle_rounds = random.randint(10, 50)
        for round_num in range(shuffle_rounds):
            button_to_press = random.choice(self.buttons)
            button_to_press.press()

    def press(self, choice):
        if choice in self.buttons_dict:
            self.buttons_dict[choice].press()

    def turn_off_all_lights(self):
        for light in self.lights:
            light.is_on = False

    def toggle_all_lights(self):
        for light in self.lights:
            light.toggle()

    def draw_curses(self, stdscr):
        self.draw_curses_lights(stdscr)
        self.draw_curses_buttons(stdscr)

    def draw_curses_lights(self, stdscr):
        # draw lights
        for row_num in range(self.light_rows):
            for col_num in range(self.light_cols):
                row = ((Light.str_height) * row_num) + Board.top_offset
                col = ((Light.str_width + 4) * col_num) + Board.left_offset
                light = self.board[row_num][col_num]
                curses_multiline_add_str(stdscr, row, col, str(light))

        # draw outline around lights
        all_light_width = ((Light.str_width + 4) * self.light_cols)
        board_width = all_light_width + Board.left_offset
        board_height = (Light.str_height * self.light_rows) + Board.top_offset
        for i in range(board_width + 1):
            char = "+" if ((i == 0) or (i == board_width)) else "-"
            stdscr.addstr(0, i, char)
            stdscr.addstr(board_height, i, char)
        for j in range(board_height + 1):
            char = "+" if ((j == 0) or (j == board_height)) else "|"
            stdscr.addstr(j, 0, char)
            stdscr.addstr(j, board_width, char)

    def draw_curses_buttons(self, stdscr):
        board_height = (Light.str_height * self.light_rows) + Board.top_offset
        button_light_row_spacing = 2
        button_row = board_height + button_light_row_spacing
        for i in range(len(self.buttons)):
            col = (Button.str_width + 2) * i
            stdscr.addstr(button_row, col, str(self.buttons[i]))

    def is_game_over(self):
        """
        all lights must be on for the game to be over
        """
        for light in self.lights:
            if not light.is_on:
                return False
        return True

    def reset(self):
        self = Board(self.light_rows, self.light_cols, self.num_buttons)
