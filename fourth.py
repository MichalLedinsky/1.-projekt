
def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se král nebo jezdec může přesunout na danou pozici.

    :param figurka: Slovník s klíči 'typ' a 'pozice'
    :param cilova_pozice: N-tice (řádek, sloupec)
    :param obsazene_pozice: Množina obsazených pozic
    :return: True, pokud je tah možný, jinak False
    """
    aktualni_pozice = figurka["pozice"]
    typ = figurka["typ"]

    # 1. KROK: Je cílová pozice na šachovnici?
    radek, sloupec = cilova_pozice

    if not (1 <= radek <= 8 and 1 <= sloupec <= 8):
        return False

    # 2. KROK: Je cílová pozice volná?
    if cilova_pozice in obsazene_pozice:
        return False

    # Rozdíly mezi aktuální a cílovou pozicí
    rozdil_radku = abs(radek - aktualni_pozice[0])
    rozdil_sloupcu = abs(sloupec - aktualni_pozice[1])

    # 3. KROK: Pohyb podle typu figury
    if typ == "král":
        # Král se může pohnout o 1 pole všemi směry.
        if (rozdil_radku <= 1 and rozdil_sloupcu <= 1
                and (rozdil_radku + rozdil_sloupcu > 0)):
            return True

    elif typ == "jezdec":
        # Jezdec se pohybuje ve tvaru L.
        if ((rozdil_radku == 2 and rozdil_sloupcu == 1)
                or (rozdil_radku == 1 and rozdil_sloupcu == 2)):
            return True

    return False


if __name__ == "__main__":
    kral = {"typ": "král", "pozice": (4, 4)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    obsazene_pozice = {(4, 4), (5, 5), (3, 5)}

    # Testy pro krále
    print(je_tah_mozny(kral, (5, 5), obsazene_pozice))  # False (obsazeno)
    print(je_tah_mozny(kral, (5, 4), obsazene_pozice))  # True
    print(je_tah_mozny(kral, (6, 6), obsazene_pozice))  # False
    print(je_tah_mozny(kral, (0, 4), obsazene_pozice))  # False

    # Testy pro jezdce
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (5, 5), obsazene_pozice))  # False
    print(je_tah_mozny(jezdec, (4, 6), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (10, 3), obsazene_pozice)) # False
