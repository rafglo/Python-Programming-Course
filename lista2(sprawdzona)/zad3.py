import zipfile
import os
import datetime


def ziping(in_path, out_path):
    """
    Function:
    Funkcja tworząca kopię zip z danego katalogu

    Input:
    in_path(string) - ścieżka do katalogu, którego kopię chcemy stworzyć
    out_path(string) - ścieżka do kopii zip

    """
    cat_name = os.path.basename(in_path)
    date = str(datetime.date.today())
    zip_name = date + "_ " + cat_name + ".zip"
    zip_path = out_path + "\\" + zip_name
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        for root, dirs, files in os.walk(in_path):
            for file in files:
                zip_file.write(os.path.join(root, file), os.path.basename(os.path.join(root, file)))
    zip_file.close()

