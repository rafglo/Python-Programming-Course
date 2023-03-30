from PIL import Image
def min_jpg(in_path, size, out_path):
    """
    Function:
    Funkcja tworząca minaturę obrazu, o danym rozmiarze

    Input:
    in_path(string) - scieżka do obrazu
    size(tuple) - krotka określająca rozmiar tworzonej miniatury
    out_path(string) - ścieżka wyjściowa miniatury

    """
    image = Image.open(in_path)
    image.thumbnail(size)
    image.save(out_path)
    image.show()

