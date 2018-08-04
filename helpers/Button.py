from helpers.Light import Light


class Button(object):
    """

    """
    def __init__(self, identifier, lights):
        self.identifier = identifier
        self.lights = lights
        self.validate()

    def validate(self):
        assert(isinstance(self.identifier, str))
        assert(isinstance(self.lights, list))
        for light in self.lights:
            assert(isinstance(light, Light))

    def press(self):
        for light in self.lights:
            light.toggle()
