# 2689 - Pal XXL

def solutie(numar):
    lista = []
    
    for indice in range(numar):
        lista.append(int(input()))
        
    numar_str = ""
    
    for indice in range(numar):
        numar_str += str(lista[indice])
        
    if numar_str == numar_str[::-1]:
        return "DA"
    else:
        return "NU"

if __name__ == "__main__":
    numar = int(input())
    
    print(solutie(numar))