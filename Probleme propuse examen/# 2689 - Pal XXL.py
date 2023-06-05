# 2689 - Pal XXL

def validareDate(numar, key):
    match key:
        case 'case1':
            try:
                number = int(numar)

                if number < 1 or number > 1_000:
                    raise ValueError("Number is outside the valid range.")

                print("Valid numbers entered:", number)
                
                return int(numar)

            except ValueError as e:
                print("Invalid input:", str(e))
                return
        case 'case2':
            try:
                number = int(numar)

                if number < 0 or number > 9:
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
        
    numar_str = ""
    
    for indice in range(numar):
        numar_str += str(lista[indice])
        
    if numar_str == numar_str[::-1]:
        print("DA") 
    else:
        print("NU")

if __name__ == "__main__":
    numar = input()
    
    numar = validareDate(numar, 'case1')
    
    if numar is not None:
        solutie(numar)