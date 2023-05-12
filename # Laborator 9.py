# Laborator 9

lista_legaturi = [[0, 1], 
                  [0, 2], 
                  [1, 2], 
                  [1, 3], 
                  [3, 4]]

# Defineste matricea in forma unei matrici de adiacenta
def matriceAdiacenta(lista_legaturi: list) -> list:
    nr_noduri = 0
    
    for linie in lista_legaturi:
        for element in linie:
            if element > nr_noduri:
                nr_noduri = element
                
    nr_noduri += 1
    
    matrice = [[0 for coloana in range(nr_noduri)] for rand in range(nr_noduri)]
    
    # print(matrice)
    
    for lista_aux in lista_legaturi:
        matrice[lista_aux[0]][lista_aux[1]], matrice[lista_aux[1]][lista_aux[0]] = 1, 1
        
    return matrice
    
# Definirea listei de adiacenta
def listaAdiacenta(matrice_adiacenta: list):
    lista_adiacenta = [(rand, coloana) for rand in range(len(matrice_adiacenta)) for coloana in range(len(matrice_adiacenta)) if matrice_adiacenta[rand][coloana] != 0 and coloana > rand]
    
    return lista_adiacenta

    
if __name__ == "__main__":
    matrice_adiacenta = matriceAdiacenta(lista_legaturi)
    
    print('Matricea de adiacenta: ')
    for linie in matrice_adiacenta:
        print(*linie, end='\n')
        
    lista_adiacenta = listaAdiacenta(matrice_adiacenta)
    
    print('Lista de adiacenta: ')
    for linie in lista_adiacenta:
        print(f'{linie}', end=' ')
                
