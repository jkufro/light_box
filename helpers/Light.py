from helpers.common import *


class Light(object):
    """
 __
[&&]
[&&]
 ||

 __
[  ]
[__]
 ||

    """
    on = " __ \n[&&]\n[&&]\n || "
    off = " __ \n[  ]\n[__]\n || "
    str_height = 4
    str_width = 4

    def __init__(self, row, col, is_on=True):
        self.row = row
        self.col = col
        self.is_on = is_on
        self.validate()

    def validate(self):
        assert(isinstance(self.is_on, bool))

    def toggle(self):
        self.is_on = not self.is_on

    def draw_curses(self, stdscr):
        curses_multiline_add_str(stdscr, self.row, self.col, str(self))

    def __repr__(self):
        return Light.on if self.is_on else Light.off
