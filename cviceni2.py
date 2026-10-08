def vynasob_xty_prvek(seznam, x, nasobek):
    """
    funkce vezme x-ty prvek ze seznamu(zadano jako 1 pro prvni prvek),
    vynasobi ho pomoci * nasobek a ulozi zpet do seznamu na puvodni pozici.
    Pozor, seznam muze mit mene prvku nez x
    """

    if len(seznam) <= x:
        print("V seznamu neni dostatek prvku")
        return seznam

    x-= 1
    if x < 0:
        print("Zadany index je zaporny")
        return seznam

    seznam[x] *= nasobek
    return seznam

def spocitej_prumer(seznam):
    """
    funkce spocita prumer cisel v seznamu
    """
    pocet = len(seznam)
    if pocet <= 0:
        print("Seznam je prazdny")
        return None
    suma = sum(seznam)
    return suma / pocet


def formatuj_text(student):
    znamky = student["znamky"]
    prumer = spocitej_prumer(znamky)
    prumer = round(prumer, 1)
    return f"Jmeno: {student['jmeno']}, Prijmeni: {student['prijmeni']}, Vek: {student['vek']}, Znamky: {student['znamky']}, Prumer: {prumer}"
  


if __name__ == "__main__":

    student = {"jmeno": "Jan", "prijmeni": "Novak", "vek": 21, "znamky": [1, 2, 1, 1, 3, 2]}
    print(formatuj_text(student))

    #seznam = vynasob_xty_prvek;([1, 2, 3, 4, 5], 3, 10)
    #print(seznam) # [1, 2, 30, 4, 5]

    #prumer=spocitej_prumer(seznam)
    #print (prumer)


#vek = input("Zadej svuj vek: ")
#vek = 1

#vek = int(vek)

#if vek >= 21:
#  print("Muzes pit v USA")
#else:
#  print("Dej si colu")

#print(f"Za rok ti {bude vek}")

#seznam = [1, 2, 3, "ctyri", 5]
#print(seznam)
#seznam.append("ahoj")
#print(seznam[2])

#print(f"Seznam ma {len(seznam)} prvku")
