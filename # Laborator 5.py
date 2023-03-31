# Laborator 5

# Exemplul 1
# Se da o lista de numere intregi. Sa se calculeze maximul si minimul produselor care se pot obtine cu numerele din lista respectiva.

def ex1_var1(lista: list) -> int:
    max1 = max(lista)
    min1 = min(lista)
    
    max2, min2 = -999_999_999, 999_999_999
    
    for element in lista:
        if element > max2 and element != max1:
            max2 = element
        if element < min2 and element != min1:
            min2 = element
            
    prod_max = max1 * max2
    prod_min = min1 * min2
    
    return prod_max, prod_min


if __name__ == '__main__':
    print("Exemplul 1:")
    
    n = int(input("Introduceti numarul de elemente al listei: "))
    lista = []
    
    for indice in range(n):
        lista.append(int(input(f'Introduceti elementul {indice + 1} al listei: ')))
        
    prod_max = ex1_var1(lista)[0]
    prod_min = ex1_var1(lista)[1]
    
    print(f'Produsul maxim este: {prod_max}\nProdusul minim este: {prod_min}')