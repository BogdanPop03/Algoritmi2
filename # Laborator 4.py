# Laborator 4

# Problema 1

def prob1():
    rest = int(input("Introduceti restul: "))
    
    lista_monede = [1, 2, 5, 10, 20, 50, 100]
    lista_rezultat = [0] * len(lista_monede)
    
    for index, val in enumerate(reversed(lista_monede)):
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
            
if __name__ == "__main__":
    # Problema 1
    print("Problema 1:")
    print("Se introduce de la tastatura un rest monetar. Sa se determine una din combinatiile in care se poate oferi restul, cu ajutorul metodei Greedy.")
    prob1()