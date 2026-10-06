cislo = int(input("Zadej celé číslo: "))

if cislo % 2 == 0:
    liche_nebo_sude = "sudé"
else:
    liche_nebo_sude = "liché"

print(f"Číslo {cislo} je {liche_nebo_sude}.")
