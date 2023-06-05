# 0086 - Half Sort

def validareDate(numar, key):
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

def solutie(numar):
    lista = []
    
    for indice in range(numar):
        element = input()
        
        element = validareDate(element, 'case2')
        
        if element is not None:
            lista.append(element)
        else:
            return
        
    lista[:len(lista) // 2] = sorted(lista[:len(lista) // 2])
    lista[len(lista) // 2:] = sorted(lista[len(lista) // 2:], reverse=True)
    
    print(*lista, sep = ' ') 

if __name__ == "__main__":
    numar = input()
    
    numar = validareDate(numar, 'case1')
    
    if numar is not None:
        solutie(numar)