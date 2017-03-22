# https://pl.python.org/forum/index.php?action=printpage;topic=2731.0
# '''
# Zliczanie ile razy dana litera wystepuje w wyrazie.
# '''

tresc = 'aaAA asyyds '
def stat(words):
    abc = {}
    for x in words:
        if not x in abc:
            abc[x] = 1
        else:
            abc[x] += 1
    return abc

# print stat(tresc)

# a, b = 0, 1
# # --print (a, b)
# while b < 3:
#     print b
#     a, b = b, a + b
#

# def funkcja(arg1, arg2=1, arg3=[3]):
#     print arg1, arg2, arg3
#     return 4
# ret = funkcja("jeden", 2)
# print (funkcja(1, 2, 3), ret)

class Figura:
    '''Pierwsza klasa'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def info(self):
        print(self.x, self.y)
    def zmien(self, x, y):
        self.x = x
        self.y = y
#
# o = Figura(1, -1)
# o.info()
# o.zmien(2,3)
# o.info()
#
class Okrag(Figura):
    '''Okrag'''
    def __init__(self):
        self.x, self.y, self.r = 0, 0, 1
        Figura.__init__
    def info(self):
        print('x = %i, y = %i, r = %i' % (self.x, self.y, self.r))
    def przesun(self, dx, dy):
        self.info()
        self.x, self.y = self.x + dx, self.y + dy
        self.info()

o = Okrag()
o.przesun(10,15)
# o.info()
# o.zmien(2,3)
# o.info()
#
