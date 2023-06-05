# 2841 - Gen Mat 27

def validareDate(numar):
    try:
        number = int(numar)

        if number < 2 or number > 20:
            raise ValueError("Number is outside the valid range.")

        print("Valid numbers entered:", number)

        return int(numar)

    except ValueError as e:
        print("Invalid input:", str(e))
        return


def solutie(numar1, numar2):
    matrice = []
    aux = 0

    for indice1 in range(numar1):
        linie = []
        for indice2 in range(numar2):
            aux += 1
            if aux * 2 % 5 == 0:
                aux += 1
            linie.append(aux * 2)
        matrice.append(linie)

    for indice in range(numar1):
        print(*matrice[indice], sep=', ')


if __name__ == "__main__":
    numar1, numar2 = input(), input()
    
    numar1, numar2 = validareDate(numar1), validareDate(numar2)

    if numar1 is not None and numar2 is not None:
        solutie(numar1, numar2)