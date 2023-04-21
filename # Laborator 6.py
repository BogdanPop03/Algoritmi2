# Laborator 6

# Selection sort

def selectionSort(lista: list) -> list:
    dim = len(lista)
    
    for i in range(dim):
        minIndexValue = i
        
        for j in range(i + 1, dim):
            if lista[j] < lista[minIndexValue]:
                minIndexValue = j
                
        if minIndexValue != i:
            lista[i], lista[minIndexValue] = lista[minIndexValue], lista[i]
        
    return lista

# Dictionaries

employee1 = {
    'id': 14,
    'name': 'John Doe',
    'age': 36,
    'position': 'Business Manager'
}

employee2 = {
    'id': 2,
    'name': 'Jane Doe',
    'age': 20,
    'position': 'N/A'
}

employee3 = {
    'id': 110,
    'name': 'John Smith',
    'age': 40,
    'position': 'Software Developer'
}

employee4 = {
    'id': 40,
    'name': 'Jane Smith',
    'age': 35,
    'position': 'Engineer'
}

lista = [employee1, employee2, employee3, employee4]
idCautat = 5

def dictionarySearch():
    for indice in range(len(lista)):
        if lista[indice]['id'] == idCautat:
            return lista[indice]['position']
    else:
        return None
        