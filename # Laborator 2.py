# Laborator 2

# Greedy

def citire():
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


def masini1():
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


def masini2():
    timp, timp_masini = citire()
    
    timp_masini = sortare(timp_masini)
    
    count = 0
    
    lista_finala = []
    
    for masina in timp_masini:
        timp -= masina
        if timp < 0:
            break
        else:
            count += 1
            lista_finala.append(masina)
            
    return count, lista_finala, timp


# Recursivitate

def suma_lista1(lista: list, indice: int):
    if indice > 0:
        return lista[indice] + suma_lista1(lista, indice - 1)
    else:
        return lista[0]
    

def suma_lista2(lista: list):
    if len(lista) == 1:
        return lista[0]
    else:
        return suma_lista2(lista[:len(lista) // 2]) + suma_lista2(lista[len(lista) // 2:])
    

def suma_lista3(lista: list):
    if len(lista) == 1:
        if lista[0] % 2 == 0:
            return lista[0]
        else:
            return 0
    else:
        return suma_lista3(lista[:len(lista) // 2]) + suma_lista3(lista[len(lista) // 2:])
    

def suma_lista4(lista: list):
    if len(lista) == 1:
        if lista[0] % 2 == 0:
            return 1
        else:
            return 0
    else:
        return suma_lista4(lista[:len(lista) // 2]) + suma_lista4(lista[len(lista) // 2:])


if __name__ == "__main__":
    # Greedy
    '''
    print("Greedy:")
    print("\nVarianta cu WHILE.")
    print(masini1(), sep='\n', end='\n') 
    print("\nVarianta cu FOR.")
    print(masini2(), sep='\n', end='\n')
    '''
    
    # Recursivitate
    print("Recursivitate:")
    numar_elemente = int(input("Introduceti numarul de elemente al listei: "))
    lista = []
    
    for indice in range(numar_elemente):
        lista.append(int(input(f'Introduceti elementul {indice + 1} al listei: ')))
        
    print("\nVersiunea 1:")    
    print(f'Rezultatul este: {suma_lista1(lista, len(lista) - 1)}')
    
    print("\nVersiunea 2 (Divide et Impera):")
    print(f'Rezultatul este: {suma_lista2(lista)}')
    
    print("\nVersiunea 3 (suma pare):")
    print(f'Rezultatul este: {suma_lista3(lista)}')
    
    print("\nVersiunea 4 (numarare pare):")
    print(f'Rezultatul este: {suma_lista4(lista)}')