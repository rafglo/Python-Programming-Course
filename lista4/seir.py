import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import sys

def seir(x, t, beta, sigma, gamma):
    """
    Function
    Funkcja opisująca model SEIR układem równań różniczkowych zwyczajnych, używana tylko jako argument funkcji rozwiązującej te równania.

    Input
    x(list) - lista parametrów początkkowych, odpowiednio (N - wielkość populacji, S - susceptible, czyli narażeni na zarażenie, E - exposed, czyli zarażeni, którzy jeszcze nie zarażają, 
    I - infectious, czyli zarażeni, którzy zarażają, R - recovered, wyleczeni, którzy z powrotem już się nie zarażą)
    t(list) - odcinki czasu, dla których funkcja będzie różniczkowana
    beta(float) - wskaźnik infekcji, tempo jej rozprzestrzeniania się
    sigma(float) - wskaźnik inkubacji, odwrotność czasu inkubacji, po którym zarażeni zaczynają zarażać
    gamma(float) - wskaźnik wyzdrowień, odwrotność czasu infekcji

    Output
    (list) - lista zwracająca pochodne funkcji S(t), E(t), I(t), R(t)

    """
    N, S, E, I, R = x
    N = S + E + I + R
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [N, dSdt, dEdt, dIdt, dRdt]

def arguments():
    """
    Function
    Funkcja dzieląca argumenty podane przez użytkownika w wierszu poleceń

    Output
    (list) - lista parametrów (nseir(list) - parametry początkowe N, S, E, I, R; bsg(list) - parametry beta, sigma, gamma)

    """
    nseir = []
    bsg = ()
    if __name__ == "__main__":
        try:
            nseir = [float(sys.argv[i]) for i in range(1,6)]
            bsg = tuple((float(sys.argv[i]) for i in range(6, 9)))
        except:
            raise TypeError("Podałeś za mało argumentów")
    return [nseir, bsg]

def seir_plot(days, args=arguments()):
    """
    Function
    Funkcja obliczająca równania różniczkowe modelu SEIR i rysująca wykres epidemii

    Input
    days(int) - liczba dni, dla której chcemy zasymulować epidemię
    args(list) - argument opcjonalny, zastosowanie znajduje w module seir_wrapper jako lista argumentów domyślnych, w razie gdyby użytkownik nie podał ich w wierszu poleceń

    """
    for n in args[0]:
        if not(n.is_integer()) or n < 0:
            raise TypeError("Parametry N, S, E, I, R muszą być liczbami naturalnymi")
    if args[0][0] != sum(args[0][i] for i in range(1,5)):
        raise ValueError("Wielkość populacji N musi być równa S + E + I + R")
    for n in args[1]:
        if type(n) != float or n < 0:
            raise TypeError("Parametry beta, sigma, gamma muszą być liczbami zmiennoprzecinkowymi (float) dodatnimi")
    t = np.linspace(1, days, days)
    sols = odeint(seir, args[0], t, args[1])
    plt.plot(t, sols[:, 1], "b", label="S")
    plt.plot(t, sols[:, 2], "m", label="E")
    plt.plot(t, sols[:, 3], "y", label="I")
    plt.plot(t, sols[:, 4], "r", label="R")
    plt.legend(loc="best")
    plt.xlabel("t")
    plt.grid()
    plt.title("Model SEIR epidemii")
    plt.xlabel("Czas (dni)")
    plt.ylabel("Liczba ludności")
    plt.show()

if __name__ == "__main__":
    seir_plot(150)
