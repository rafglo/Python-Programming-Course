import qrcode, os, cv2

def qr_generator(message, out_path, name, fill_color = "black", back_color = "white"):
    """
    Function - qr_generator
    Funkcja kodująca daną wiadomość w kod QR z personalizowanym kolorem tła i wypełnienia

    Input:
    message(string) - wiadomość, którą chcemy zakodować
    out_path(string) - ścieżka dla wyniku (kodu QR w postaci pliku PNG)
    name(string) - nazwa pliku zawierającego kod
    fill_color(string) - kolor wypełnienia
    back_color(string) - kolor tła

    """
    qr_code = qrcode.QRCode() #ustawiamy parametry: version - rozmiar (od 1 do 40), box_size - rozmiar kwadratów, border - rozmiar obramowania
    qr_code.add_data(message) #do kodu dodajemy wiadomość, która będzie zakodowana
    qr_code.make(fit=True) #tworzymy kod QR, w taki sposób, że nawet jeśli wiadomość będzie zbyt mała na rozmiar kodu, zostanie on wypełniony kwadratami
    img = qr_code.make_image(fill_color=fill_color, back_color=back_color) #tworzymy obraz kodu z edytowanym kolorem wypełnienia i tła
    qr_name = name + ".png"
    qr_path = os.path.join(out_path, qr_name)
    img.save(qr_path)

qr_generator("cose237e6238e76", r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 3", "por", "blue", "pink")

def qr_decode(qr_path):
    """
    Function - qr_decode
    Funkcja dekodująca wiadomość z kodu QR

    Input:
    qr_path(string) - ścieżka do pliku zawierającego kod QR

    Output:
    data(string) - odszyfrowana wiadomość
    
    """
    qr_code = cv2.imread(qr_path)
    decoder = cv2.QRCodeDetector()
    data, _, _ = decoder.detectAndDecode(qr_code)
    return data
print(qr_decode(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 3\por.png"))

