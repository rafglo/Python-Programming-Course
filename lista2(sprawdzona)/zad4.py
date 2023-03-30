from PyPDF2 import PdfWriter, PdfReader
def divider2(x, n):
    """
    Function:
    Funkcja dzieląca listę [1,2,..,x] na listy o danej długości

    Input:
    x(integer) - górny zakres listy
    n(integer) - podział listy

    Output:
    list1(list) - podział początkowej listy

    """
    list1 = []
    if x % n !=0:
        for i in range(1, n * (x//n), n):
            list1.append(list(range(i, i+n)))
        list1.append(list(range(n * (x//n) + 1, x+1)))
    else:
        for i in range(1, x+1, n):
            list1.append(list(range(i, i+n)))
    return list1


def pdf_div(in_path, n):
    """
    Function:
    Funkcja dzieląca plik PDF na pliki o danej liczbie stron

    Input:
    in_path(string) - ścieżka do pliku PDF
    n(integer) - liczba stron, które ma zawierać każdy z plików podzielonych

    """
    file = PdfReader(open(in_path, "rb"))
    rng = divider2(len(file.pages), n)
    for r in rng:
        output = PdfWriter()
        for page in range(len(file.pages)):
            if (page+1) in r:
                output.add_page(file.pages[page])
        with open("PDF" + "[" + str(r[0]) +"-" + str(r[-1]) + "]" + ".pdf", "wb") as OutputStream:
            output.write(OutputStream)




        
