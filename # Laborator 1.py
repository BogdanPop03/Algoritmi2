# Laborator 1

'''
Problema 1:
Sa se defineasca o functie care primeste ca parametrii o lista de numere naturale si un numar natural. Sa se verifice daca n primit ca parametru exista in lista si in cazul in care acesta exista sa se returneze true iar in cazul in care acesta nu exista sa se returneze false.
'''


def Problema1(lista: list, numar: int) -> bool:
    ok = False
    
    for indice in range(len(lista)):
        if lista[indice] == numar:
            ok = True
            break
        
    return ok


'''
Problema 2:
Sa se defineasca o functie care primeste ca parametru o matrice si un numar si reintoarce True daca imi gaseste numarul in matrice si False in caz contrar.
'''


def Problema2(matrice: list, numar: int) -> bool:
    for linie in matrice:
        for indice in range(len(linie)):
            if linie[indice] == numar:
                return True
    
    return False


'''
Problema 3:
Sa se defineasca o functie recursiva care calculeaza factorialul unui numar.
Sa se defineasca o functie recursiva care calculeaza suma cifrelor unui numar.
'''

def Problema3_1(numar: int) -> int:
    if numar == 0:
        return 1
    else:
        return numar * Problema3_1(numar - 1)
    

def Problema3_2(numar: int) -> int:
    if numar == 0:
        return 0
    else:
        return numar % 10 + Problema3_2(numar // 10)
    
    
def Problema3_3(numar: int) -> int:
    if numar > 9:
        if numar % 10 == 0:
            return 1 + Problema3_3(numar // 10)
        else:
            return Problema3_3(numar // 10)
    else:
        if numar == 0:
            return 1
        else:
            return 0
        
        
def Problema4(lista: list) -> list:
    flag = True
    
    while(flag):
        flag = False
        for indice in range(len(lista) - 1):
            if lista[indice] > lista[indice + 1]:
                flag = True
                lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
        
    return lista


if __name__ =="__main__":
    '''
    print("Problema 1:")
    print("Varianta 1:")
    numar = int(input("Introduceti un numar: "))
    
    lista = [10, 15, 2, 20, 123, 543, 456, 76, 345, 76546, 123412]
    
    print(Problema1(lista, numar))
    
    print("Varianta 2:")
    numar_elemente = int(input("Introduceti numarul de elemente al listei: "))
    
    lista = []
    
    for indice in range(numar_elemente):
        lista.append(int(input(f'Introduceti elementeul {indice + 1} al listei: ')))
        
    numar = int(input("Introduceti numarul care va fi cautat in lista: "))
    
    print(Problema1(lista, numar))
    
    print("Problema 2:")
    print("Varianta 1:")
    
    numar = int(input("Introduceti un numar: "))
    
    matrice = [[12, 32, 45, 65, 23],
               [543, 65, 32, 32 ,56],
               [876, 45, 43, 876, 456]]
    
    print(Problema2(matrice, numar))
    
    print("Varianta 2:")
    numar_lin = int(input("Introduceti numarul de linii al matricei: "))
    numar_col = int(input("Introduceti numarul de coloane al matricei: "))
    
    matrice = []
    
    for indice_lin in range(numar_lin):
        linie = []
        for indice_col in range(numar_col):
            linie.append(int(input(f'Introduceti elementul [{indice_lin}][{indice_col}] al matricei: ')))
        matrice.append(linie)
        
    numar = int(input("Introduceti numarul cautat: "))
    
    print(Problema2(matrice, numar))
    '''
    '''
    print("Problema 3:")
    print("Functia 1:")
    
    numar = int(input("Introduceti un numar: "))
    
    print(Problema3_1(numar))
    
    print("Functia 2:")
    
    numar = int(input("Introduceti un numar: "))
    
    print(Problema3_2(numar))
    
    print("Functia 3:")
    
    numar = int(input("Introduceti un numar: "))
    
    print(Problema3_3(numar))
    '''
    
    lista = [2, 5, 4, 3, 7]
    print(*Problema4(lista))