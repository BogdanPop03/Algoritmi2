# Laborator 7

# Problema 1
# Cautarea intr-o lista simpla
# Definiti o functie care face cautarea intr-o lista si returneaza pozitia elementului cautat sau -1 daca acesta nu exista

def problema1(lista: list, element: int) -> int:
    if element in lista:
        return lista.index(element)
    else:
        return -1
    

if __name__ == "__main__":
    # Problema 1
    nr_elemente = int(input("Introduceti numarul de elemente al listei: "))
    
    lista = [int(input(f'Introduceti elementul {indice} al listei: ')) for indice in range(nr_elemente)]
    
    element_cautat = int(input("Introduceti numarul cautat: "))
    
    print(problema1(lista, element_cautat))