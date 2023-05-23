import tkinter as tk
from tkinter import ttk
import requests
import  json
from PIL import ImageTk, Image
import tkinter.font as font

def downloading_table(table_path, out_path):
    """
    Function
    Funckcja pobierająca tabelę z kursami walut

    Input
    table_path(string) - ścieżka do tabeli (strona NBP)
    out_path(string) - ścieżka do folderu, w którym zostanie zapisany plik

    Output
    out_path(string) - ścieżka do folderu, w którym zostanie zapisany plik

    """
    try:
        response = requests.get(table_path)
        with open(out_path, "wb") as file:
            file.write(response.content)
    except:
        pass
    return out_path

def reading_json(path):
    """
    Function
    Funkcja czytająca plik z tabelą o rozszerzeniu json

    Input
    path(string) - ścieżka do pliku json z tabelą

    Output
    table(list) - lista słowników zawierających informacje o walutach

    """
    with open(path, "r", encoding="utf-8") as file:
        table = json.load(file)
    return table

def table_parsing(path):
    """
    Function 
    Funkcja rozdzielająca informacje z listy słowników, będącej wynikiem poprzedniej funkcji

    Input
    path(string) - ścieżka do pliku json z tabelą

    Output
    currencies(list) - lista nazw walut
    codes(list) - lista kodów walut
    mids(list) - lista kursów walut

    """
    table = reading_json(downloading_table(r"http://api.nbp.pl/api/exchangerates/tables/a/", path))
    rates = table[0]["rates"]
    currencies = ["złoty (Polska)"]
    codes = ["PLN"]
    mids = ["1.00"]
    for rate in rates:
        currencies.append(rate["currency"])
        codes.append(rate["code"])
        mids.append(rate["mid"])
    return currencies, codes, mids

currencies, codes, mids = table_parsing(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\tabela.json")
tuple(currencies)
tuple(codes)
tuple(mids)

root = tk.Tk()
root.title("Kalkulator walutowy")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = screen_width // 3
window_height = screen_height // 3
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 5\dolars.jpg"))
background_label = ttk.Label(root, image=background_image)
background_label.place(x=0, y=0)


frame5 = ttk.Frame(root)
frame5.pack(pady=30)
frame1 = ttk.Frame(frame5)
frame1.pack(side=tk.TOP)
frame2 = ttk.Frame(frame5)
frame2.pack(pady=5)
amount_int = tk.IntVar()
amount_label = ttk.Label(frame1, text="Wpisz liczbę pieniędzy", font=("Montserrat", 9))
amount_label.pack(side=tk.LEFT, padx=43)
amount_entry = ttk.Entry(frame2, textvariable=amount_int, width=30)
amount_entry.pack(padx=10, side=tk.LEFT)

frame6 = ttk.Frame(root)
frame6.pack(pady=30)
frame3 = ttk.Frame(frame6)
frame3.pack(pady=5)
frame4 = ttk.Frame(frame6)
frame4.pack()
currency1_label = ttk.Label(frame1, text="Wybierz walutę początkową", font=("Montserrat", 9))
currency1_label.pack(side=tk.RIGHT, padx=33)
currency1_string = tk.StringVar()
currency1_combobox = ttk.Combobox(frame2, textvariable=currency1_string, width=30)
currency1_combobox["values"] = currencies
currency1_combobox["state"] = "readonly"
currency1_combobox.pack(padx=10, side=tk.RIGHT)


pick_frame = ttk.Frame(root)
pick_frame.pack()
result_string = "0"
result_label = ttk.Label(frame3, text="Wynik konwersji", font=("Montserrat", 9))
result_label.pack(side=tk.LEFT, padx=57)
result_window = ttk.Label(frame4, text=result_string, borderwidth=2, relief="solid", width = 30)
result_window.pack(padx=10, side=tk.LEFT)

def calculations():
    """
    Function
    Funkcja przeliczająca ilość danej waluty na inną walutę

    Output
    output(float) - ilość pieniędzy po przeliczeniu na daną walutę

    """
    amount = amount_int.get()
    currency1 = currency1_string.get()
    currency2 = currency2_string.get()
    cur1_index = currencies.index(currency1)
    cur2_index = currencies.index(currency2)
    cur1_rate = float(mids[cur1_index])
    cur2_rate = float(mids[cur2_index])
    in_zloty = amount * cur1_rate
    output = in_zloty / cur2_rate
    return output

def result_change():
    """
    Function
    Funkcja zmieniająca tekst wyświetlający się w oknie z wynikiem

    """
    result_window.config(text=str(calculations()))

def close():
    """
    Funkcja zamykająca okno

    """
    root.destroy()


currency2_label = ttk.Label(frame3, text="Wybierz walutę końcową", font=("Montserrat", 9))
currency2_label.pack(side=tk.RIGHT, padx=40)
currency2_string = tk.StringVar()
currency2_combobox = ttk.Combobox(frame4, textvariable=currency2_string, width=30)
currency2_combobox["values"] = currencies
currency2_combobox["state"] = "readonly"
currency2_combobox.pack(padx=10, side=tk.RIGHT)

my_font = font.Font(family="Montserrat", size=9)

buttons_frame = ttk.Frame(root)
buttons_frame.pack(pady=30)
start_button = ttk.Button(buttons_frame, text="Oblicz", font=my_font, command=result_change)
start_button.pack(side=tk.LEFT, padx=65)
exit_button = ttk.Button(buttons_frame, text="Zakończ", font=my_font, command=close)
exit_button.pack(side=tk.RIGHT, padx=70)



root.mainloop() 
