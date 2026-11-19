class InvalidData(Exception):
    pass


class Osoba:
    def __int__(self, jmeno, telefon, email):
        self.jmeno = jmeno
        self.telefon = telefon
        self.email = email

    @property
    def jmeno(self):
        return self.__jmeno
    
    @property
    def telefon(self):
        return self.__telefon

    @property
    def email(self):
        return self.__email

    @jmeno.setter
    def jmeno(self, hodnota)
        if hodnota.replace(" ", "").isalpha():
            self.__jmeno = hodnota
        else:
            raise InvalidData("Jmeno muze obsahovat pouze pismena")

    @telefon.setter
    def telefon(self, hodnota)
        if hodnota.isnumeric():
            self.__telefon = hodnota
        else:
            raise InvalidData("Cislo muze obsahovat pouze cislice")

    @email.setter
    def email(self, hodnota)
        if hodnota.replace(" ", "").isalpha():
            self.__email = hodnota
        else:
            raise InvalidData("Jmeno muze obsahovat pouze pismena")
    
def __str__(self):
    return f"Osoba: {self.jmeno}, {self.telefon}, {self.email}"

if __name__ == "__main__":
#    O = Osoba("Jan Novák", "004225877845", "jan@novak.cz")
#    o.jmeno = "4357253"
#    o.telefon = "asfarsfsf"
#    o.email = "xxxl"
#    print(o)
osoby = [ ]

print(osoby)
