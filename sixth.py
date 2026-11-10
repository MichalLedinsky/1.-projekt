
import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stáhne zadanou URL pomocí requests.get(),
    zkontroluje návratový kód response.status_code,
    a pokud je 200, najde všechny výskyty <a href="url">
    a získané URL vrátí jako seznam.
    """
    hrefs = []

    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        # Vyhledání všech odkazů ve tvaru <a href="...">
        while '<a href="' in content:
            start = content.find('<a href="') + len('<a href="')
            end = content.find('"', start)

            if end == -1:
                break

            href = content[start:end]
            hrefs.append(href)

            content = content[end + 1:]

    else:
        raise Exception(f"Chyba při stahování stránky. HTTP kód: {response.status_code}")

    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)

        print(hrefs)

    except Exception as e:
        print(f"Program skončil chybou: {e}")
