# 0255 - Termen n din sirul Fibonacci

def validareDate(numar):
    try:
        number = int(numar)

        if number < 1 or number > 500_000_000:
            raise ValueError("Number is outside the valid range.")

        print("Valid number entered:", number)
        
        return int(numar)

    except ValueError as e:
        print("Invalid input:", str(e))
        return

def solutie(numar):
    fibo1, fibo2 = 0, 1
    fibo3 = 0
    
    if numar == 1:
        print(fibo1)
    elif numar == 2:
        print(fibo2)
    else:
        for i in range(2, numar ):
            fibo3 = fibo1 + fibo2
            fibo1, fibo2 = fibo2, fibo3
    
        print(fibo3)

if __name__ == "__main__":
    numar = input()
    
    numar = validareDate(numar)
    
    if numar is not None:
        solutie(numar)