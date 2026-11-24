def bin_to_dec(binarni_cislo):
    # Funkce převede binární číslo na decimální.
    # Vstup může být typu str nebo int.
    # Například: 10011101 -> 157
    return int(str(binarni_cislo), 2)


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    assert bin_to_dec("10011101") == 157
    assert bin_to_dec(10011101) == 157


if __name__ == "__main__":
    test_bin_to_dec()
    print("Všechny testy proběhly úspěšně!")
