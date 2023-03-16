import  random
import math

class Vector:

    def __init__(self, args = 3):
        """
        Function:
        Funkcja inicializująca obiekt klasy Vector o atrybutach:
        self.wektor(list) - lista opisująca wektor
        self.rozmiar(integer) - rozmiar wektora

        Input:
        args(integer) - rozmiar wektora (domyślnie 3)

        """
        self.wektor = []
        self.rozmiar = args
        for i in range(args):
            self.wektor.append(0)
    
    def generowanie(self):
        """
        Function:
        Funkcja losowo generująca wspołrzędne wektora z danego zakresu

        Output:
        self.wektor(list) - wektor po wygenerowaniu jego elementów

        """
        for i in range(self.rozmiar):
            self.wektor[i] = random.uniform(0,10)
        return self.wektor

    def wczytywanie(self, wektor2):
        """
        Function:
        Funkcja zmieniająca istniejący wektor w zadany wektor

        Input:
        wektor2(list) - wektor, w który chcemy zamienić obiekt

        Output:
        self.wektor(list) - wektor początkowy po zamianie na dany wektor

        """
        if type(wektor2) is list:
            if self.rozmiar == len(wektor2):
                for i in range(len(wektor2)):
                    self.wektor[i] = wektor2[i]
                return self.wektor
            else:
                raise ValueError("Długości wektorów są różne. Nie można ich zamienić.")
        else:
            raise TypeError("Podany argument nie jest wektorem (listą)")
    
    def __str__(self):
        """
        Function:
        Funkcja pozwalająca wyświetlić obiekt klasy Vector za pomocą funkcji print()

        Output:
        str(self.wektor)(string) - ciąg znaków, opisujący obiekt klasy Vector

        """ 
        return str(self.wektor)

    def __add__(self, wektor2):
        """
        Function:
        Funkcja pozwalająca na dodanie dwóch wektorów za pomocą "+"

        Input:
        wektor2(list) - wektor, który chcemy dodać do istniejącego wektora

        Output:
        suma(list) - wektor, będący sumą danego wektora i wektora początkowego
        """
        if type(wektor2) is list: 
            if self.rozmiar == len(wektor2):
                for i in range(self.rozmiar):
                    self.wektor[i] += wektor2[i]
                return self.wektor
            else:
                raise ValueError("Wektory mają różne rozmiary")
        else:
            raise TypeError("Podany argument nie jest wektorem (listą)")
        
    def __sub__(self, wektor2):
        """
        Function:
        Funkcja pozwalająca odejomwanie dwóch wektorów za pomocą "-"

        Input:
        wektor2(list) - wektor, który chcemy odjąć od istniejącego wektora 

        Output:
        roznica(list) - wektor, będący różnicą danego wektora i wektora początkowego

        """
        if type(wektor2) is list: 
            if self.rozmiar == len(wektor2):
                for i in range(self.rozmiar):
                    self.wektor[i] -= wektor2[i]
                return self.wektor
            else:
                raise ValueError("Wektory mają różne rozmiary")
        else:
            raise TypeError("Podany argument nie jest wektorem (listą)")
    
    def mnozenie(self, skalar):
        """
        Function:
        Funkcja pozwalająca na pomnożenie wektora przez skalar

        Input:
        skalar(float) - skalar, przez który chcemy pomnożyć istniejący wektor

        Output:
        self.wektor(list) - wektor początkowy pomnożony przez dany skalar

        """
        for i in range(len(self.wektor)):
            self.wektor[i] *= skalar
        return self.wektor

    def dlugosc(self):
        """
        Function:
        Funkcja zwracająca długość wektora 

        Output:
        math.sqrt(suma_kwadratow)(float) - długość wektora 

        """
        suma_kwadratow = 0
        for i in range(self.rozmiar):
            suma_kwadratow += self.wektor[i]**2
        return math.sqrt(suma_kwadratow)
    
    def suma_elementow(self):
        """
        Function:
        Funkcja zwracająca sumę elementów wektora

        Output:
        suma(float) - suma elementów wektora

        """
        suma = 0
        for i in range(self.rozmiar):
            suma += self.wektor[i]
        return suma
    
    def __mul__(self, wektor2):
        """
        Function:
        Funkcja obliczająca iloczyn skalarny dwóch wektorów za pomocą "*"

        Input:
        wektor2(list) - wektor, przez który wektor początkowy jest przemnażany skalarnie

        Output:
        suma(float) - wynik mnożenia skalarnego danego wektora i wektora początkowego

        """
        if type(wektor2) is list:
            if self.rozmiar == len(wektor2):
                suma = 0
                for i in range(len(self.wektor)):
                    suma += self.wektor[i] * wektor2[i]
                return suma
            else:
                raise ValueError("Wektory mają różne rozmiary")
        else:
            raise TypeError("Podany argument nie jest wektorem")
    
    def __getitem__(self, indeks):
        """
        Function:
        Funkcja pozwalająca wybrać element (współrzędną) wektora o podanym indeksie

        Input:
        indeks(integer) - indeks wybieranego z wektora elementu (współrzędnej)

        Output:
        self.wektor[indeks](float) - wybrany element (współrzędna) z wektora

        """
        return self.wektor[indeks]

    def __contains__(self, element):
        """
        Funkcja sprawdzająca, czy wektor zawiera podany element

        Input:
        element(float) - element sprawdzany

        Output:
        True(boolean) - jeśli element należy do wektora
        False(boolean) - jeśli element nie należy do wektora

        """
        if element in self.wektor:
            return True
        else:
            return False
print("---------------------------------------------------")
wektor = Vector(3) #tworzenie wektora (złożonego z samych zer)
print("Wynik generowania wektora:", wektor.generowanie())
wektor2 = [3.0,4.0,5.0]
print("Wynik wczytywania wektor2 w miejsce wektora początkowego:", wektor.wczytywanie(wektor2))
print("Wynik dodawania wektor2 do wektor:", wektor + wektor2)
print("Wynik odejmowania wektor2 od wektora:", wektor - wektor2)
print("Wynik mnożenia wektora przez skalar:", wektor.mnozenie(3))
print("Długość wektora:", wektor.dlugosc())
print("Suma elemnentów wektora:", wektor.suma_elementow())
print("Wynik mnożenia skalarnego wektora przez wektor2:", wektor * wektor2)
print("Wypisanie danego elementu wektora:", wektor[2])
print("Czy element znajduje się w wektorze:", 2 in wektor)

