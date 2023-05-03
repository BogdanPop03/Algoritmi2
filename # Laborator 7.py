# Laborator 7

# Problema 1
# Cautarea intr-o lista simpla
# Definiti o functie care face cautarea intr-o lista si returneaza pozitia elementului cautat sau -1 daca acesta nu exista

def problema1(lista: list, element: int) -> int:
    if element in lista:
        return lista.index(element)
    else:
        return -1
    

# Problema 2
# CNP

def generareC(CNP: str) -> str:
    numar = "279146358279"
    
    suma = int(0)
    
    for indice in range(len(CNP)):
        suma += int(CNP[indice]) * int(numar[indice])
        
    rest = suma % 11
    
    if rest < 10:
        return str(rest)
    else:
        return str(1)
    

def problema2(sex: str, an: int, luna: int, zi: int, judet: int, nnn: int) -> str:
    CNP: str = ""
    
    if sex == "M" or sex == "m" or sex == "masculin":
        if an < 2000:
            CNP += '1'
        else:
            CNP += '5'
    else:
        if an < 2000:
            CNP += '2'
        else:
            CNP += '6'
            
    if an < 2000:
        an = an - 1900
    else:
        an = an - 2000
    if an < 10:
        CNP += '0' + str(an)
    else:
        CNP += str(an)
        
    if luna < 10:
        CNP += '0' + str(luna)
    else:
        CNP += str(luna)
    
    if zi < 10:
        CNP += '0' + str(zi)
    else:
        CNP += str(zi)
        
    if judet < 10:
        CNP += '0' + str(judet)
    else:
        CNP += str(judet)
        
    if nnn < 10:
        CNP += '00' + str(nnn)
    elif 9 < nnn < 100:
        CNP += '0' + str(nnn)
    else:
        CNP += str(nnn)
        
    CNP += generareC(CNP)
    
    return CNP
    

if __name__ == "__main__":
    nr = int(input("Introduceti numarul sarcinii dorite: "))
    
    if nr == 1:
        # Problema 1
        nr_elemente = int(input("Introduceti numarul de elemente al listei: "))
        
        lista = [int(input(f'Introduceti elementul {indice} al listei: ')) for indice in range(nr_elemente)]
        
        element_cautat = int(input("Introduceti numarul cautat: "))
        
        print(problema1(lista, element_cautat))
        
    if nr == 2:
        # Problema 2
        print(problema2("m", 2003, 1, 2, 24, 502))