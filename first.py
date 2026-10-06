def sude_nebo_liche(cislo):
    x = cislo % 2

    if x == 0:
        print(f"Cislo {cislo} je sude")
    else:
        print(f"Cislo {cislo} je liche")


if __name__ == "__main__":
    sude_nebo_liche(5)
    sude_nebo_liche(1000000)
