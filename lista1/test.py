from Vectorclass import Vector
print("---------------------------------------------------")
wektor = Vector(3) #tworzenie wektora (złożonego z samych zer)
print("Wynik generowania wektora:", wektor.generowanie())
wektor2 = [3,4,5]
print("Wynik wczytywania wektor2 w miejsce wektora początkowego:", wektor.wczytywanie(wektor2))
print("Wynik dodawania wektor2 do wektor:", wektor + wektor2)
print("Wynik odejmowania wektor2 do wektor:", wektor - wektor2)
print("Wynik mnożenia wektora przez skalar:", wektor.mnozenie(3))
print("Długość wektora:", wektor.dlugosc())
print("Suma elemnentów wektora:", wektor.suma_elementow())
print("Wynik mnożenia skalarnego wektora przez wektor2:", wektor * wektor2)
print("Wypisanie danego elementu wektora:", wektor[2])
print("Czy element znajduje się w wektorze:", 2 in wektor)
