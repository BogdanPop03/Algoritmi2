# Laborator 3

# Se da o matrice patratica. Sa se determine elementul care contine valoarea maxima si elementul care contine valoarea minima.

def prob1_ver1(matrice: list) -> int:
    maxim = 0
    minim = 1_000_000_000
    
    for indice_lin in range(len(matrice)):
        for indice_col in range(len(matrice[0])):
            if matrice[indice_lin][indice_col] > maxim:
                maxim = matrice[indice_lin][indice_col]
            if matrice[indice_lin][indice_col] < minim:
                minim = matrice[indice_lin][indice_col]
    
    return maxim, minim


def prob1_ver2(matrice: list) -> int:
    maxim = max(matrice)
    minim = min(matrice)
    
    return maxim, minim
    