# 0069 - Oglindit

def validareDate(numar):
    try:
        number = int(numar)

        if number < 0 or number > 1_000_000_000:
            raise ValueError("Number is outside the valid range.")

        print("Valid number entered:", number)
        
        return str(numar)

    except ValueError as e:
        print("Invalid input:", str(e))
        return

def solutie(numar):
    numar = numar[::-1]
    
    print(numar)

if __name__ == "__main__":
    numar = input()
    
    numar = validareDate(numar)
    
    if numar is not None:
        solutie(numar)