# 0086 - Half Sort

def solutie(numar):
    lista = []
    
    for indice in range(numar):
        lista.append(int(input()))
        
    lista[:len(lista) // 2] = sorted(lista[:len(lista) // 2])
    lista[len(lista) // 2:] = sorted(lista[len(lista) // 2:], reverse=True)
    
    return lista

if __name__ == "__main__":
    numar = int(input())
    
    print(solutie(numar))