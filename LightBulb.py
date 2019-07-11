MAX_VALUE, MIN_VALUE = 255, 0

from RGBColor import RGBColor


class LightBulb:
    _color = RGBColor
    _switched_on = False

    def __init__(self, red=0, green=0, blue=0, color=None):
        if color:
            print(type(color), color)
            self._color = RGBColor(color._red, color._green, color._blue)
            #if isinstance(color, RGBColor):
                #self.color = RGBColor(color)
        if 0 <= (red and green and blue) <= 255:
            self._color = RGBColor(red, green, blue)
        else:
            self.color = RGBColor(0, 0, 0)
        self._switched_on = False

    def __copy__(self, other_bulb):
        if isinstance(other_bulb, LightBulb):
            self._color = RGBColor.__copy__(self, other_bulb._color)
            self._switched_on = other_bulb._switched_on

    def is_switched_on(self):
        return bool(self._switched_on)

    def switch_light(self):
        self._switched_on = not self._switched_on



    def __repr__(self):
        """
        Representation (toString) method of the class LightBulb
        :return: view on print for an object of class LightBulb.
        """
        on_or_off = None
        if (LightBulb.is_switched_on == True):
            on_or_off = "On"
        else:
             on_or_off = "Off"
        return (f'{self.__class__.__name__}'
            f'(' f'{self._color._red!r}, {self._color._green!r}, {self._color._blue!r}) {on_or_off!r}')