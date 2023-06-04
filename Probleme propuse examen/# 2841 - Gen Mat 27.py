# 2841 - Gen Mat 27

def solutie(numar1, numar2):
    matrice = []
    aux = 0
    
    for indice1 in range(numar1):
        linie = []
        for indice2 in range(numar2):
            aux += 1
            linie.append(aux * 2)
        matrice.append(linie)
    
    return matrice

if __name__ == "__main__":
    numar1, numar2 = int(input()), int(input())
    
    matrice = solutie(numar1, numar2)
    
    for indice in range(numar1):
        print(*matrice[indice], sep=', ')