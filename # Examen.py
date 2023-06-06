# Examen 6.06.2023

# Problema 1
# Se da un numar natural n.
# Sa se afiseze termenul n al sirului lui Fibonacci.


# Validare date problema 1
def validareDate_problema1(numar):
    try:
        number = int(numar)

        if number < 1 or number > 500_000_000:
            raise ValueError("Number is outside the valid range.")

        print("Valid number entered:", number)
        
        return int(numar)

    except ValueError as e:
        print("Invalid input:", str(e))
        return
    

# Solutie problema 1
def problema1(numar) -> int:
    fib1, fib2, fib3 = 0, 1, 0
    
    if numar == 1:
        return fib1
    elif numar == 2:
        return fib2
    else:
        for indice in range(3, numar + 1):
            fib3 = fib1 + fib2
            fib1, fib2 = fib2, fib3
            
        return fib3

# Problema 2
# Se da un vector n cu elemente numerre intregi, n fiind numar par.
# Sa se ordoneze crescator elementele din prima jumatate a vectorului si descrescator elementele din a doua jumatate.


# Validare date problema 2
def validareDate_problema2(numar, key: str):
    match key:
        case 'case1':
            try:
                number = int(numar)

                if number < 1 or number > 100 or number % 2:
                    raise ValueError("Number is outside the valid range.")

                print("Valid numbers entered:", number)
                
                return int(numar)

            except ValueError as e:
                print("Invalid input:", str(e))
                return
        case 'case2':
            try:
                number = int(numar)

                if number < -1_000_000_000 or number > 1_000_000_000:
                    raise ValueError("Number is outside the valid range.")

                print("Valid numbers entered:", number)
                
                return int(numar)

            except ValueError as e:
                print("Invalid input:", str(e))
                return


# Solutie problema 2
def problema2(lista: list) -> list:
    lista[:len(lista) // 2] = sorted(lista[:len(lista) // 2])
    lista[len(lista) // 2:] = sorted(lista[len(lista) // 2:], reverse=True)
    
    return lista


# Problema 3
# Scrieti un program care citeste de la tastatura un numar natural n si construieste in memorie un tablou bidimensional, cu n liniii si n coloane astfel:
#   1. prima coloana contine, in ordine strict crescatoare, numerele naturale din intervalul [1, n];
#   2. toate elementele ultimei linii au valoarea n;
#   3. oricare alt element este obtinut prin insumarea celor doua elemente vecine cu el, aflate pe coloana anterioara, unul pe aceeasi linie cu el, iar celalat pe linia urmatoare


# Validare date problema 3
def validareDate_problema3(numar):
    try:
        number = int(numar)

        if number < 2 or number > 20:
            raise ValueError("Number is outside the valid range.")

        print("Valid number entered:", number)
        
        return int(numar)

    except ValueError as e:
        print("Invalid input:", str(e))
        return
    
    
# Solutie problema 3
def problema3(numar) -> list:
    matrice = []

    for indice_linie in range(numar):
        linie = []
        for indice_coloana in range(numar):
            linie.append(0)
        matrice.append(linie)
    
    for indice in range(numar):
        matrice[indice][0] = indice + 1
        matrice[numar - 1][indice] = numar
        
    for indice_coloana in range(1, numar):
        for indice_linie in range(0, numar - 1):
            matrice[indice_linie][indice_coloana] = matrice[indice_linie][indice_coloana - 1] + matrice[indice_linie + 1][indice_coloana - 1]
            
    return matrice


if __name__ == "__main__":
    # Problema 1
    print("Problema 1")
    numar_problema1: str = input("Introduceti numarul pentru problema 1: ")
    
    numar_problema1 = validareDate_problema1(numar_problema1)
    
    if numar_problema1 is not None:
        print(f'Raspuns problema 1: {problema1(numar_problema1)}')
    
    # Problema 2
    print("\nProblema 2")
    
    numar_elemente_problema2: str = input("Introduceti numarul de elemente ale vectorului pentru problema 2: ")
    
    numar_elemente_problema2 = validareDate_problema2(numar_elemente_problema2, 'case1')
    
    if numar_elemente_problema2 is not None:
        lista_problema2: list = []
        
        for indice in range(numar_elemente_problema2):
            element: str = input(f'Introduceti elementul [{indice}] al vectorului pentru problema 2: ')
            
            element = validareDate_problema2(element, 'case2')
            
            if element is not None:
                lista_problema2.append(element)
            else:
                break
        else:
            raspuns_problema2: list = problema2(lista_problema2)
            
            print("Raspuns problema2: ", end = '')
            print(*raspuns_problema2, sep = ' ')
    
    # Problema 3
    print("\nProblema 3")
    
    numar_problema3: str = input("Introduceti numarul de linii si coloane pentru problema 3: ")
    
    numar_problema3 = validareDate_problema3(numar_problema3)
    
    if numar_problema3 is not None:
        raspuns_problema3: list = problema3(numar_problema3)
        
        for indice in range(numar_problema3):
            print(*raspuns_problema3[indice], sep=' ')