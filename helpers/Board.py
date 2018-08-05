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
    button_light_row_spacing = 2

    def __init__(self, light_rows=5, light_cols=5, num_buttons=8):
        self.light_rows = light_rows
        self.light_cols = light_cols
        self.num_buttons = num_buttons
        self.board_height = ((Light.str_height * self.light_rows) +
                             Board.top_offset)
        self.button_row = self.board_height + Board.button_light_row_spacing
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
                l_row = ((Light.str_height) * row_num) + Board.top_offset
                l_col = ((Light.str_width + 4) * col_num) + Board.left_offset
                light = Light(l_row, l_col)
                self.lights.append(light)
                row.append(light)
            self.board.append(row)

    def make_buttons(self):
        starting_identifier = ord("A")
        shuffled_lights = divide_with_overlap(self.lights, self.num_buttons)
        for button_num in range(self.num_buttons):
            identifier = chr(starting_identifier + button_num)
            lights = shuffled_lights[button_num]
            row = self.button_row
            col = (Button.str_width + 2) * button_num
            button = Button(identifier, lights, row, col)
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
        for light in self.lights:
            light.draw_curses(stdscr)
        self.draw_curses_outline(stdscr)
        for button in self.buttons:
            button.draw_curses(stdscr)

    def draw_curses_outline(self, stdscr):
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
