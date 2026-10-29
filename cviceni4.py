import sys

def inkrementuj_cisla(data):
    pass

def nacti_radky(file_name):
    pass

def zapis_radky(file_name, data):
    pass

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print(f'Pouziti: python {sys.argv[0]} jmeno_souboru')
        sys.exit()

    file_name = sys.argv[1]  # data.txt

    try:
        data = nacti_radky(file_name)
    except FileNotFoundError:
        print(f'Soubor {file_name} neexistuje')
        
    data = inkrementuj_cisla(data)

    name = file_name.split('.')  #  name = ['data', 'csv']

    file_name2 = name[0] + '2.' + name[1]  #  'data2.txt'
    zapis_radky(file_name2, data)
