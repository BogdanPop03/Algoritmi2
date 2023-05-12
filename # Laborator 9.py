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
    
    
if __name__ == "__main__":
    matrice = matriceAdiacenta(lista_legaturi)
    
    for linie in matrice:
        print(linie, end='\n')
                
