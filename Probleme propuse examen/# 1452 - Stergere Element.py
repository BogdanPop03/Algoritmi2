# 1452 - Stergere Element

def solutie(numar, index):
    lista = []
    
    for indice in range(numar):
        lista.append(int(input()))
    
    del lista[index - 1]
    
    return lista

if __name__ == "__main__":
    numar = int(input())
    index = int(input())
    
    print(solutie(numar, index))