# 0274 - 3 Minime

def solutie(numar):
    numar1, numar2, numar3 = 0, 0, 0
    
    lista = []
    
    for indice in range(numar):
        lista.append(int(input()))
    
    lista.sort()
    
    numar1, numar2, numar3 = lista[2], lista[1], lista[0]
    
    return numar1, numar2, numar3

if __name__ == "__main__":
    numar = int(input())
    
    print(solutie(numar))