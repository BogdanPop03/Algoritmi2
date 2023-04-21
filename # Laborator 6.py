# Laborator 6

# Selection sort

def selectionSort(lista: list) -> list:
    dim = len(lista)
    
    for i in range(dim):
        minIndexValue = i
        
        for j in range(i + 1, dim):
            if lista[j] < lista[minIndexValue]:
                minIndexValue = j
                
        if minIndexValue != j:
            lista[i], lista[minIndexValue] = lista[minIndexValue], lista[i]
        
    return lista