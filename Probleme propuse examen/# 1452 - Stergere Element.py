# 1452 - Stergere Element

def validareDate(numar, indice, key):
    match key:
        case 'case1':
            try:
                number = int(numar)
                index = int(indice)

                if number < 1 or number > 1_000:
                    raise ValueError("Number is outside the valid range.")
                if index < 1 or index > number:
                    raise ValueError("Number is outside the valid range.")

                print("Valid numbers entered:", number, index)
                
                return int(numar), int(indice)

            except ValueError as e:
                print("Invalid input:", str(e))
                return
        case 'case2':
            try:
                number = int(numar)
                # index = int(indice)

                if number < -1_000_000 or number > 1_000_000:
                    raise ValueError("Number is outside the valid range.")
                # if index < 0 or index > number - 1:
                #     raise ValueError("Number is outside the valid range.")

                print("Valid numbers entered:", number)
                
                return int(numar)

            except ValueError as e:
                print("Invalid input:", str(e))
                return

def solutie(numar, index):
    lista = []
    
    for indice in range(numar):
        element = input()
        
        element = validareDate(element, 0, 'case2')
        
        if element is not None:
            lista.append(element)
        if element is None:
            return
    
    del lista[index - 1]
    
    print(*lista, sep = ' ') 

if __name__ == "__main__":
    numar = int(input())
    indice = int(input())
    
    numar, indice = validareDate(numar, indice, 'case1')
    
    if numar is not None and indice is not None:
        solutie(numar, indice)