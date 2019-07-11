from LightBulb import LightBulb

class Disco:
    _bulb1 = LightBulb
    _bulb2 = LightBulb
    _bulb3 = LightBulb
    _bulb4 = LightBulb

    def __init__(self, b1, b2, b3, b4):
        if isinstance((b1 and b2 and b3 and b4), LightBulb):
            self._bulb1 = LightBulb.__copy__(self, b1)
            self._bulb2 = LightBulb.__copy__(self, b2)
            self._bulb3 = LightBulb.__copy__(self, b3)
            self._bulb4 = LightBulb.__copy__(self, b4)

    def switch_bulb(self, num):
        if num == 1:
            self._bulb1.switch_light()
        elif num == 2:
            self._bulb2.switch_light()
        elif num == 3:
            self._bulb3.switch_light()
        elif num == 4:
            self._bulb4.switch_light()
        else:
            input("Please, input number from 1 till 4")

    def turn_all_on(self):
        if not self._bulb1.is_switched_on:
            self._bulb1.switch_light()
        elif not self._bulb2.is_switched_on:
            self._bulb2.switch_light()
        elif not self._bulb3.is_switched_on:
            self._bulb3.switch_light()
        elif not self._bulb4.is_switched_on:
            self._bulb4.switch_light()

    def turn_all_off(self):
        if self._bulb1.is_switched_on:
            self._bulb1.switch_light()
        elif self._bulb2.is_switched_on:
            self._bulb2.switch_light()
        elif self._bulb3.is_switched_on:
            self._bulb3.switch_light()
        elif self._bulb4._is_switched_on:
            self._bulb4.switch_light()

    def are_all_on(self):
        return bool(self._bulb1._is_switched_on and self._bulb2._is_switched_on \
                    and self._bulb3._is_switched_on and self._bulb4._is_switched_on)

    def are_all_off(self):
        return bool(not self._bulb1._is_switched_on and not self._bulb2._is_switched_on() \
                    and not self._bulb3._is_switched_on() and not self._bulb4.is_switched_on())

    def all_same_color(self):
        return bool(self._bulb1.equals(self._bulb2) and \
                    self._bulb1.equals(self._bulb3) and self._bulb1.equals(self._bulb4))
