# 4207 - SumProdRec

def validareDate(numar):
    try:
        number = int(numar)

        if number < 2 or number > 10_000:
            raise ValueError("Number is outside the valid range.")

        print("Valid numbers entered:", number)

        return int(numar)

    except ValueError as e:
        print("Invalid input:", str(e))
        return

def solutie(numar):
    if numar == 1:
        return 0
    else:
        return (numar - 1) * numar + solutie(numar - 1)

if __name__ == "__main__":
    numar = input()
    
    numar = validareDate(numar)
    
    if numar is not None:
        print(solutie(numar))