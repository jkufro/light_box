from helpers.Light import Light
from helpers.Button import Button
from helpers.common import *
import random


class Board(object):
    """

    """
    def __init__(self, light_rows=5, light_cols=5, num_buttons=8):
        self.light_rows = light_rows
        self.light_cols = light_cols
        self.num_buttons = num_buttons
        self.lights = []
        self.buttons = []
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
            self.buttons.append(Button(identifier, lights))

    def mix_board(self):
        shuffle_rounds = random.randint(10, 50)
        for round_num in range(shuffle_rounds):
            button_to_press = random.choice(self.buttons)
            button_to_press.press()

    def draw_curses(self, stdscr):
        for row_num in range(self.light_rows):
            for col_num in range(self.light_cols):
                curses_row = (Light.str_height) * row_num
                curses_col = (Light.str_width + 2) * col_num
                light = self.board[row_num][col_num]
                curses_multiline_add_str(stdscr,
                                         curses_row,
                                         curses_col,
                                         str(light))

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
