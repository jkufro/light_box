from helpers.Light import Light


class Button(object):
    """

[ A ] [ B ] [ C ] [ D ] [ E ] [ F ] [ G ]


    """
    str_width = 5

    def __init__(self, identifier, lights):
        self.identifier = identifier
        self.lights = lights
        self.validate()

    def validate(self):
        assert(isinstance(self.identifier, str))
        assert(len(self.identifier) == 1)
        assert(isinstance(self.lights, list))
        for light in self.lights:
            assert(isinstance(light, Light))

    def press(self):
        for light in self.lights:
            light.toggle()

    def __repr__(self):
        return "[ %s ]" % self.identifier
