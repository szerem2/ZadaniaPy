class Samochod:
    def naprzod(self):
        print ('samochod')

class Okret:
    def naprzod(self):
        print ('okret')

class Amfibia(Okret, Samochod):
    '''Amfibia'''


amf = Amfibia()
amf.naprzod()
