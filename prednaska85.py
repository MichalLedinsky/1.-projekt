class ZapornyZustatek(Exception):
    pass

class BankovniUcet:
    def __int__(self):
        self.__zustatek = 0

    @property
    def zustatek(self):
        return self.__zustatek

    @zustatek.setter
    def zustatek(self, hodnota):
        if hodnota < 0:
            raise ZapornyZustatek("Nelze nastavit zaporny zustatek")
        self._zustatek = hodnota
