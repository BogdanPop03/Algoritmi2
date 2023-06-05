# 3268 - CMMDC CMMMC

def validareDate(numar):
    try:
        number = int(numar)

        if number < 0 or number > 1_000_000_000:
            raise ValueError("Number is outside the valid range.")

        print("Valid number entered:", number)
        
        return int(numar)

    except ValueError as e:
        print("Invalid input:", str(e))
        return

def solutie(numar1, numar2):
    cmmdc, cmmmc = 0, 0
    copie1, copie2 = numar1, numar2
    
    while numar1 != numar2:
        if numar1 > numar2:
            numar1 -= numar2
        else:
            numar2 -= numar1
    
    cmmdc = numar1
    
    cmmmc = (copie1 * copie2) // cmmdc
    
    
    print(cmmdc, cmmmc)

if __name__ == "__main__":
    numar1 = input()
    numar2 = input()
    
    numar1, numar2 = validareDate(numar1), validareDate(numar2)
    
    if numar1 is not None and numar2 is not None:
        solutie(numar1, numar2)