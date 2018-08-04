

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

    def __init__(self, is_on=True):
        self.is_on = is_on
        self.validate()

    def validate(self):
        assert(isinstance(self.is_on, bool))

    def toggle(self):
        self.is_on = not self.is_on

    def __repr__(self):
        return Light.on if self.is_on else Light.off
