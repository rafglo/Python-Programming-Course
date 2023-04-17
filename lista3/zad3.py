from PyPDF2 import PdfMerger
import aspose.words as aw
from datetime import date 
import time, os

def pdf_combine(in_paths, out_path, pdf_name):
    """
    Function - pdf_combine
    Funkcja łącząca kilka plików PDF w jeden

    Input:
    in_paths(list) - lista ścieżek do plików PDF
    out_path(string) - ścieżka do pliku końcowego
    pdf_name(string) - nazwa pliku końcowego

    """
    output = PdfMerger()
    for file in in_paths:
        output.append(file)
    output.write(out_path + pdf_name + ".pdf")
    output.close()
pdf_combine([r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\PDF[1-6].pdf", r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\PDF[7-12].pdf", r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\PDF[13-18].pdf", r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\PDF[19-21].pdf"],r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem", "\lacznik")

def compare_pdf(path1, path2):
    """
    Function - compare_pdf
    Funkcja porównująca dwa pliki PDF

    Input:
    path1(string) - ścieżka do pierwszego pliku PDF
    path2(string) - ścieżka do drugiego pliku PDF

    Output:
    False(boolean) - jeśli pliki są różne
    True(boolean) - jeśli pliki są takie same

    """
    pdf1 = aw.Document(path1) #ładujemy pliki PDF
    pdf1_name = os.path.basename(path1) #wyodrębniamy nazwy plików
    pdf2 = aw.Document(path2)
    pdf2_name = os.path.basename(path2)
    pdf1.save(pdf1_name + ".docx", aw.SaveFormat.DOCX) #zapijsujemy zawartość pliku PDF do pliku o rozszerzeniu .docx
    doc1 = aw.Document(pdf1_name + ".docx") #ładujemy dokumenty wordowskie
    pdf2.save(pdf2_name + ".docx", aw.SaveFormat.DOCX)
    doc2 = aw.Document(pdf2_name + ".docx")

    options = aw.comparing.CompareOptions() #Ustawiamy opcje porównywania
    options.ignore_formatting = True
    options.ignore_headers_and_footers = True
    options.ignore_case_changes = True
    options.ignore_tables = True
    options.ignore_fields = True
    options.ignore_comments = True
    options.ignore_textboxes = True
    options.ignore_footnotes = True

    doc1.compare(doc2, "user", date.today(), options) #Funkcja porównująca dwa dokumenty i zapisująca zmiany w doc1

    if doc1.revisions.count > 0: #jeśli zmian jest więcej niż 0, to dokumenty są różne, jeśli nie, są sobie równe
        return False
    else:
        return True
    
start = time.time()
compare_pdf(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lacznik.pdf", r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 2\maturka.pdf")
print("Program trwał: " + str(time.time() - start) + " sekund.")
