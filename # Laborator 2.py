# Laborator 2

from typing import Union

# Greedy

def citire() -> Union[int, list]:
    timp = int(input("Introduceti numarul de minute in care se poate lucra la masini: "))
    
    nr_masini = int(input("Introduceti numarul de masini: "))
    
    timp_masini = []
    
    for indice in range(nr_masini):
        timp_masini.append(int(input(f'Introduceti timpul alocat (in minute) reparatiei masinii cu numarul {indice + 1}: ')))
        
    return timp, timp_masini
    

def sortare(lista: list) -> list:
    flag = True
    
    while flag:
        flag = False
        
        for indice in range(len(lista) - 1):
            if lista[indice] > lista[indice + 1]:
                lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
                flag = True
                
    return lista


def masini1() -> Union[int, list, int]:
    timp, timp_masini = citire()
    
    timp_masini = sortare(timp_masini)
    
    indice = 0
    count = 0
    
    lista_finala = []
    
    while timp > 0 and timp >= timp_masini[indice]:
        lista_finala.append(timp_masini[indice])
        count += 1
        timp -= timp_masini[indice]
        indice += 1
    
    return count, lista_finala, timp


def masini2() -> Union[int, list, int]:
    timp, timp_masini = citire()
    
    timp_masini = sortare(timp_masini)
    
    count = 0
    lista_finala = []
    
    for masina in timp_masini:
        timp -= masina
        if timp < 0:
            return count, lista_finala, timp + masina
        else:
            count += 1
            lista_finala.append(masina)


# Recursivitate

def suma_lista1(lista: list, indice: int) -> int:
    if indice > 0:
        return lista[indice] + suma_lista1(lista, indice - 1)
    else:
        return lista[0]
    

def suma_lista2(lista: list) -> int:
    if len(lista) == 1:
        return lista[0]
    else:
        return suma_lista2(lista[:len(lista) // 2]) + suma_lista2(lista[len(lista) // 2:])
    

def suma_lista3(lista: list) -> int:
    if len(lista) == 1:
        if lista[0] % 2 == 0:
            return lista[0]
        else:
            return 0
    else:
        return suma_lista3(lista[:len(lista) // 2]) + suma_lista3(lista[len(lista) // 2:])
    

def suma_lista4(lista: list) -> int:
    if len(lista) == 1:
        if lista[0] % 2 == 0:
            return 1
        else:
            return 0
    else:
        return suma_lista4(lista[:len(lista) // 2]) + suma_lista4(lista[len(lista) // 2:])


if __name__ == "__main__":
    # Greedy
    print("Greedy:")
    print("\nVarianta cu WHILE.")
    aux1 = masini1()
    print(f'Rezultatul este: \n\t * numarul de masini la care s-a lucra este: {aux1[0]}; \n\t * lista cu durata masinilor la care s-a lucrat este: {aux1[1]} ; \n\t * timpul ramas (in minute) este: {aux1[2]}.') 
    print("\nVarianta cu FOR.")
    aux2 = masini2()
    print(f'Rezultatul este: \n\t * numarul de masini la care s-a lucra este: {aux2[0]}; \n\t * lista cu durata masinilor la care s-a lucrat este: {aux2[1]}; \n\t * timpul ramas (in minute) este: {aux2[2]}.') 
    
    # Recursivitate
    print("Recursivitate:")
    numar_elemente = int(input("Introduceti numarul de elemente al listei: "))
    lista = []
    
    for indice in range(numar_elemente):
        lista.append(int(input(f'Introduceti elementul {indice + 1} al listei: ')))
        
    print("\nVersiunea 1 (suma):")    
    print(f'Rezultatul este: {suma_lista1(lista, len(lista) - 1)}')
    
    print("\nVersiunea 2 (suma Divide et Impera):")
    print(f'Rezultatul este: {suma_lista2(lista)}')
    
    print("\nVersiunea 3 (suma pare):")
    print(f'Rezultatul este: {suma_lista3(lista)}')
    
    print("\nVersiunea 4 (numarare pare Divide et Impera):")
    print(f'Rezultatul este: {suma_lista4(lista)}')
    
    print('\n')