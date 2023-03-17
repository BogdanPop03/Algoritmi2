# Laborator 3

# Problema 1
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


# Problema 2
# Se da o matrice patratica. Sa se genereze elementele matricei dupa urmatoarele reguli:
#   1). elementele pentru care produsul indicilor este un numar par vor avea valoarea 1
#   2). elementele pentru care produsul indicilor este un numar impar vor avea valoarea 0
#   3). elementele de pe diagonala principala vor avea valoarea 2

def prob2(matrice: list) -> list:
    dim = len(matrice)
    
    for indice_lin in range(dim):
        for indice_col in range(dim):
            if indice_lin == indice_col:
                matrice[indice_lin][indice_col] = 2
            else:
                if indice_lin * indice_col % 2 == 0:
                    matrice[indice_lin][indice_col] = 1
                else:
                    matrice[indice_lin][indice_col] = 0
                    
    return matrice


# Problema 3
# 
    

if __name__ == '__main__':
    numar = int(input("Introduceti numarul problemei pe care doriti sa o rezolvati(1 -> ): "))
    
    if numar == 1:
        print("Problema 1:\nSe da o matrice patratica. Sa se determine elementul care contine valoarea maxima si elementul care contine valoarea minima.\n")
        
        nr_lin = int(input("Introduceti numarul de linii al matricei: "))
        nr_col = int(input("Introduceti numarul de coloane al matricei: "))
        
        matrice = []
        
        for indice_lin in range(nr_lin):
            linie = []
            for indice_col in range(nr_col):
                linie.append(int(input(f'Introduceti elementul [{indice_lin}][{indice_col}] al matricei: ')))
            matrice.append(linie)
        
        print("Rezolvare:")
        
        print("Versiunea 1:")
        raspuns1_prob1 = prob1_ver1(matrice)
        print(f'Maximul este: {raspuns1_prob1[0]}')
        print(f'Minimul este: {raspuns1_prob1[1]}')
        
        print("Versiunea 2:")
        raspuns2_prob1 = prob1_ver2(matrice)
        print(f'Maximul este: {raspuns2_prob1[0]}')
        print(f'Minimul este: {raspuns2_prob1[1]}')
    elif numar == 2:
        print("Problema 2:\nSe da o matrice patratica. Sa se genereze elementele matricei dupa urmatoarele reguli:\n\t1). elementele pentru care produsul indicilor este un numar par vor avea valoarea 1;\n\t2). elementele pentru care produsul indicilor este un numar impar vor avea valoarea 0;\n\t 3). elementele de pe diagonala principala vor avea valoarea 2.")
        
        nr_lin = int(input("Introduceti numarul de linii al matricei: "))
        nr_col = int(input("Introduceti numarul de coloane al matricei: "))
        
        matrice = []
        
        for indice_lin in range(nr_lin):
            linie = []
            for indice_col in range(nr_col):
                linie.append(int(input(f'Introduceti elementul [{indice_lin}][{indice_col}] al matricei: ')))
            matrice.append(linie)
            
        print("Rezolvare:")
        print("Matricea devine:")
        print(prob2(matrice))
            