# 2800 - Chenar 1

def validareDate(numar, key):
    match key:
        case 'case1':
            try:
                number = int(numar)

                if number < 3 or number > 50:
                    raise ValueError("Number is outside the valid range.")

                print("Valid numbers entered:", number)
                
                return int(numar)

            except ValueError as e:
                print("Invalid input:", str(e))
                return
        case 'case2':
            try:
                number = int(numar)

                if number < 0 or number > 104:
                    raise ValueError("Number is outside the valid range.")

                print("Valid numbers entered:", number)
                
                return int(numar)

            except ValueError as e:
                print("Invalid input:", str(e))
                return

def solutie(numar1, numar2):
    matrice = []
    
    for index1 in range(numar1):
        lista = []
        for index2 in range(numar2):
            element = input()
            
            element = validareDate(element, 'case2')
            
            if element is not None:
                lista.append(element)
            else:
                return
        matrice.append(lista)
        
    numar = matrice[numar1 - 1][numar2 - 1]
    
    for index in range(numar1):
        matrice[index][0] = numar
        matrice[index][numar2 - 1] = numar
        
    for index in range(numar2):
        matrice[0][index] = numar
        matrice[numar1 - 1][index] = numar

    for indice in range(numar1):
        print(*matrice[indice])

if __name__ == "__main__":
    numar1, numar2 = input(), input()
    
    numar1 = validareDate(numar1, 'case1')
    numar2 = validareDate(numar2, 'case2')
    
    if numar1 is not None and numar2 is not None:
        solutie(numar1, numar2)