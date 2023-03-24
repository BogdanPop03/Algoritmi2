# Laborator 4

from typing import Union

# Problema 1
def prob1():
    rest: int = int(input("Introduceti restul: "))
    
    lista_monede: list = [1, 2, 5, 10, 20, 50, 100]
    lista_rezultat: list = [0] * len(lista_monede)
    
    for index, val in enumerate(reversed(lista_monede)):
        if rest == 0:
            break
        while val <= rest and rest != 0:
            rest -= val
            lista_rezultat[index] += 1
        
    lista_rezultat = lista_rezultat[::-1]
    
    print("Este nevoie de: ", end = "")
    
    for indice in range(len(lista_rezultat)):
        if indice == 0 and lista_rezultat[indice] != 0:
            if lista_rezultat[indice] == 1:
                print(f'{lista_rezultat[indice]} moneda de 1 leu, ', end = "")
            else:
                print(f'{lista_rezultat[indice]} monede de 1 leu, ', end = "")
        elif indice == 1 and lista_rezultat[indice] != 0:
            if lista_rezultat[indice] == 1:
                print(f'{lista_rezultat[indice]} moneda de 2 lei, ', end = "")
            else:
                print(f'{lista_rezultat[indice]} monede de 2 lei, ', end = "")
        elif indice == 2 and lista_rezultat[indice] != 0:
            if lista_rezultat[indice] == 1:
                print(f'{lista_rezultat[indice]} moneda de 5 lei, ', end = "")
            else:
                print(f'{lista_rezultat[indice]} monede de 5 lei, ', end = "")
        elif indice == 3 and lista_rezultat[indice] != 0:
            if lista_rezultat[indice] == 1:
                print(f'{lista_rezultat[indice]} bancnota de 10 lei, ', end = "")
            else:
                print(f'{lista_rezultat[indice]} bancnote de 10 lei, ', end = "")
        elif indice == 4 and lista_rezultat[indice] != 0:
            if lista_rezultat[indice] == 1:
                print(f'{lista_rezultat[indice]} moneda de 20 lei, ', end = "")
            else:
                print(f'{lista_rezultat[indice]} monede de 20 lei, ', end = "")
        elif indice == 5 and lista_rezultat[indice] != 0:
            if lista_rezultat[indice] == 1:
                print(f'{lista_rezultat[indice]} moneda de 50 lei, ', end = "")
            else:
                print(f'{lista_rezultat[indice]} monede de 50 lei, ', end = "")
        elif indice == 6 and lista_rezultat[indice] != 0:
            if lista_rezultat[indice] == 1:
                print(f'{lista_rezultat[indice]} moneda de 100 lei, ', end = "")
            else:
                print(f'{lista_rezultat[indice]} monede de 100 lei, ', end = "")
                
                
# Problema 2
def prob2():
    lista: list = []
    for indice in range(3):
        lista.append(int(input(f'Introduceti elementul {indice + 1} al listei: ')))
        
    for indice in range(len(lista)):
        lista[indice] = 255 - lista[indice]

    print(*lista, sep = ", ")
    
    
# Problema 3
def prob3(numar: int) -> int:
    return 255 - numar


# Problema 4
def prob4(numar: int) -> Union[list, int]:
    if numar <= 2:
        return 1
    else:
        lista_fib: list = [0] * numar
        
        lista_fib[0], lista_fib[1] = 1, 1
        
        for indice in range(2, numar):
            lista_fib[indice] = lista_fib[indice - 1] + lista_fib[indice - 2]
            
        return lista_fib, lista_fib[numar - 1]
    
            
if __name__ == "__main__":
    numar_prob: int = int(input("Introduceti numarul problemei (1-4): "))
    
    if numar_prob == 1:
        # Problema 1
        print("Problema 1:")
        print("Cerinta: \nSe introduce de la tastatura un rest monetar. Sa se determine una din combinatiile in care se poate oferi restul, cu ajutorul metodei Greedy.\n")
        prob1()
        
    elif numar_prob == 2:
        # Problema 2
        print("Problema 2:")
        print("Cerinta: \nSe da o lista cu 3 elemente cu valori intre 0 si 255. Sa se modifice lista astfel incat valoarea de pe fiecare pozitie sa fie inversa fata de 255.\n")
        prob2()
        
    elif numar_prob == 3: 
        # Problema 3
        print("Problema 3:")
        print("Cerinta: \nSe da o functie care primeste ca parametru un numar natural. Sa se returneze 255 - numarul dat.\n")
        numar: int = int(input("Introduceti un numar natural: "))
        print(prob3(numar))
    
    elif numar_prob == 4:
        # Problema 4
        print("Problema 4:")
        print("Cerinta: \n.Se da un numar natural ca si parametru al unei functii. Sa se returneze lista primilor n termeni ai sirului lui Fibonacci si al n-lea numar din sirul lui Fibonacci.\n")
        numar: int = int(input("Introduceti un numar natural: "))
        if numar <= 2:
            print(prob4(numar))
        else:
            print(f'Lista primelor {numar} numere Fibonacci este: {prob4(numar)[0]}.\nAl {numar} - lea numar Fibonacci este: {prob4(numar)[1]}.')
            
    else:
        print("Nu ati introdus un numar valid.")