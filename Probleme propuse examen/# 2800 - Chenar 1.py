# 2800 - Chenar 1

def solutie(numar1, numar2):
    matrice = []
    
    for index1 in range(numar1):
        lista = []
        for index2 in range(numar2):
            lista.append(int(input()))
        matrice.append(lista)
        
    numar = matrice[numar1 - 1][numar2 - 1]
    
    for index in range(numar1):
        matrice[index][0] = numar
        matrice[index][numar2 - 1] = numar
        
    for index in range(numar2):
        matrice[0][index] = numar
        matrice[numar1 - 1][index] = numar

    return matrice

if __name__ == "__main__":
    numar1, numar2 = int(input()), int(input())
    
    matrice = solutie(numar1, numar2)
    
    for indice in range(numar1):
        print(*matrice[indice])