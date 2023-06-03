# 0336 - Expresie 4

def solutie(numar):
    raspuns = 0
    
    for indice in range(numar):
        raspuns += (indice + 1) * (numar - indice)

    return raspuns        

if __name__ == "__main__":
    numar = int(input())
    
    raspuns = solutie(numar)
    
    print("Raspunsul este:", raspuns)