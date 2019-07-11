from LightBulb import LightBulb
from Disco import Disco


if __name__ == '__main__':
    b1 = LightBulb(101, 201, 111)
    b2 = LightBulb(155, 220, 215)
    b3 = LightBulb(152, 221, 230)
    b4 = LightBulb(156, 250, 250)

    print(b1, b2, b3, b4)

    disco = Disco(b1, b2, b3, b4)

    a = disco.are_all_off()
    print(a)










