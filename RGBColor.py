THIRTEEN_PERCENT, FIFTY_NINE_PERCENT, ELEVEN_PERCENT = 0.3, 0.59, 0.11
MAX_VALUE, MIN_VALUE = 255, 0


# The class represents a triad RGB color.
class RGBColor(object):
    _red, _green, _blue = 0, 0, 0

    def __init__(self, red=0, green=0, blue=0):
        """
        The constructor validates parameters and
        create a new object with these parameters.
        """
        super(RGBColor, self).__init__()
        if red < MIN_VALUE or red > MAX_VALUE or green < MIN_VALUE \
                or green > MAX_VALUE or blue < 0 or blue > 255:
            self._red = 0
            self._green = 0
            self._blue = 0
        else:
            self._red = red
            self._green = green
            self._blue = blue

    def __copy__(self, color):
        """
        Copy initializer of the class RGBColor.
        """
        if isinstance(color, RGBColor):
            return RGBColor(color._red, color._green, color._blue)

    def __repr__(self):
        """
        Representation (toString) method of the class RGBColor.
        :return: view on print for an object of class RGBColor.
        """
        return (f'{self.__class__.__name__}'
                f'(' f'{self._red!r}, {self._green!r}, {self._blue!r})')

    def equals(self, other):
        """
        Equals method of the class RGBColor.
        """
        if isinstance(other, RGBColor):
            return self._red == other._red and self._green == other._green \
                  and self._blue == other._blue

    def mix(self, other):
        """
        Mix method of the class RGBColor.
        """
        self._red = round((self._red + other._red) / 2)
        self._green = round((self._green + other._green) / 2)
        self._blue = round((self._blue + other._blue) / 2)

    def convert_to_grayscale(self):
        """
        The method returns the gray value of a three color
        """
        return (self._red * THIRTEEN_PERCENT) + (self._green * FIFTY_NINE_PERCENT) + \
               (self._blue * ELEVEN_PERCENT)

    def invert(self):
        """
        Invert method of the class RGBColor.
        """
        self._red = 255 - self._red
        self._green = 255 - self._green
        self._blue = 255 - self._blue
