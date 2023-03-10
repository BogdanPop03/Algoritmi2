# Laborator 2

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


def masini1() -> int:
    timp, timp_masini = citire()
    
    timp_masini = sortare(timp_masini)
    
    indice = 0
    count = 0
    
    while timp > 0 and timp >= timp_masini[indice]:
        count += 1
        timp -= timp_masini[indice]
        indice += 1
    
    return count


def masini2() -> int:
    timp, timp_masini = citire()
    
    timp_masini = sortare(timp_masini)
    
    count = 0
    
    for masina in timp_masini:
        timp -= masina
        if timp < 0:
            break
        else:
            count += 1
            
    return count


if __name__ == "__main__":
    print(masini2())
    