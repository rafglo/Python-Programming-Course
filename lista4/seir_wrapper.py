import argparse, seir

def parsing():
    """
    Function
    Funkcja, przyjmująca parametry podane przez użytkownika w wierszu poleceń w stylu uniksowym (w dowolnej kolejności) oraz dorabiająca wartości domyślne dla tych, których nie podał

    Output
    lista parametrów (nseir(list) - parametry początkowe N, S, E, I, R; bsg(list) - parametry beta, sigma, gamma)

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-N', type=float)
    parser.add_argument('-beta', type=float)
    parser.add_argument('-I0', type=float)
    parser.add_argument('-S0', type=float)
    parser.add_argument('-E0', type=float)
    parser.add_argument('-R0', type=float)
    parser.add_argument('-gamma', type=float)
    parser.add_argument('-sigma', type=float)
    args = parser.parse_args()

    if not args.N:
        args.N = 1000.0
    if not args.beta:
        args.beta = 1.34
    if not args.I0:
        args.I0 = 0.0
    if not args.S0:
        args.S0 = args.N - 1.0
    if not args.R0:
        args.R0 = 0.0
    if not args.E0:
        args.E0 = 1.0
    if not args.gamma:
        args.gamma = 0.34
    if not args.sigma:
        args.sigma = 0.19
    
    nseir = [args.N, args.S0, args.E0, args.I0, args.R0]
    bsg = (args.beta, args.sigma, args.gamma)

    return [nseir, bsg]

argumenty = parsing()
seir.seir_plot(200, argumenty)
