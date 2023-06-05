# 0274 - 3 Minime

def validareDate(numar, key):
    if key == 'numar_elemente':
        try:
            number = int(numar)

            if number < 3 or number > 100:
                raise ValueError("Number is outside the valid range.")

            print("Valid number entered:", number)
            
            return int(numar)

        except ValueError as e:
            print("Invalid input:", str(e))
            return
    elif key == 'element':
        try:
            number = int(numar)

            if number < 0 or number > 9_999:
                raise ValueError("Number is outside the valid range.")

            print("Valid number entered:", number)
            
            return int(numar)

        except ValueError as e:
            print("Invalid input:", str(e))
            return
        

def solutie(numar):
    numar1, numar2, numar3 = 0, 0, 0
    
    lista = []
    
    for indice in range(numar):
        element = input()
        
        element = validareDate(element, 'element')
        
        if element is not None:
            lista.append(element)
        if element is None:
            return
    
    lista.sort()
    
    numar1, numar2, numar3 = lista[2], lista[1], lista[0]
    
    print(numar1, numar2, numar3) 

if __name__ == "__main__":
    numar = input()
    
    numar = validareDate(numar, 'numar_elemente')
    
    if numar is not None:
        solutie(numar)