from PyPDF2 import PdfMerger, PdfReader
from pdf2image import convert_from_path
from diff_pdf_visually import pdf_similar
def pdf_combine(in_paths, out_path, pdf_name):
    output = PdfMerger()
    for file in in_paths:
        output.append(file)
    output.write(out_path + pdf_name + ".pdf")
    output.close()
pdf_combine([r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\PDF[1-6].pdf", r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\PDF[7-12].pdf", r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\PDF[13-18].pdf", r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\PDF[19-21].pdf"],r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem", "\lacznik")
pdf_similar(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 2\maturka.pdf", r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 2\maturka.pdf")
