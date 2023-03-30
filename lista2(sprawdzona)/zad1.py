import random, string as stg

def password(dlugosc, symbols = []):
    """
    Function:
    Funkcja generująca hasło o danej liczbie znaków, (opcjonalnie z danej listy symboli)

    Input:
    dlugosc(integer) - liczba znaków, które ma zawierać hasło
    symbols(list) - lista znaków, z których ma być zbudowane hasło (domyślnie: duże i małe litery, cyfry, znaki specjalne)

    Output:
    password(string) - wygenerowane hasło

    """
    if type(symbols) is list:
        password_list = [0 for i in range(dlugosc)]
        chars = [stg.ascii_lowercase, stg.ascii_uppercase, stg.digits, stg.punctuation]
        chars_str = ""
        for i in chars:
            chars_str += i
        if len(symbols) == 0:
            ind = [i for i in range(dlugosc)]
            for symbol in chars:
                ind_1 = random.choice(ind)
                ind.remove(ind_1)
                password_list[ind_1] = random.choice(symbol)
            for ind_2 in ind:
                symbol = random.choice(chars)
                password_list[ind_2] = random.choice(symbol)
        else:
            c = 0
            for symbol in symbols:
                if str(symbol) not in chars_str or (type(symbol) is int and (symbol < 0 or symbol > 9)):
                    c += 1
            if c == 0:
                for i in range(len(password_list)):
                    password_list[i] = random.choice(symbols)
            else:
                raise TypeError("W podanej liście znaków znajduje się element, który nie może znajdować się w haśle (dopuszczane: litery(A-Z, a-z), cyfry(0-9), znaki specjalne)")
        password = ""
        for i in password_list:
            password += str(i)
        return password
    else:
        raise TypeError("Nie podano listy symboli")



    

