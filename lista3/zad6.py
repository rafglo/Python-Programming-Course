import requests
from bs4 import BeautifulSoup
import webbrowser

def wiki(n):
    """
    Function - wiki
    Funkcja proponująca użytkownikowi tytuły artykułów na wikipedii i wyświetlająca ten, który mu się spodobał.

    Input:
    n(integer) - liczba prób, które program podejmie w celu znalezienia odpowiadającego użytkownikowi artykułu

    """
    counter = 0
    while counter < n:
        counter += 1
        article_url = "https://en.wikipedia.org/wiki/Special:Random"
        article = requests.get(article_url)
        soup = BeautifulSoup(article.content, "html.parser")
        title = soup.find(id="firstHeading").text
        y_or_n = input("Tytuł artykułu to: " + title + ". Podoba ci się? (t/n)")
        if y_or_n == "t":
            webbrowser.open("https://en.wikipedia.org/wiki/" + title, new=1, autoraise=True)
            break
        else:
            continue
    else:
        print("Wygląda na to, że żaden artykuł Ci się nie spodobał :(")
wiki(5)
