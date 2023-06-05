# 0336 - Expresie 4

def validareDate(numar):
    try:
        number = int(numar)

        if number < 1 or number > 100:
            raise ValueError("Number is outside the valid range.")

        print("Valid number entered:", number)
        
        return int(numar)

    except ValueError as e:
        print("Invalid input:", str(e))
        return

def solutie(numar):
    raspuns = 0
    
    for indice in range(numar):
        raspuns += (indice + 1) * (numar - indice)

    print(raspuns)         

if __name__ == "__main__":
    numar = input()
    
    numar = validareDate(numar)
    
    if numar is not None:
        solutie(numar)