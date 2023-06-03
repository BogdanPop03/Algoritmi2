# 0255 - Termen n din sirul Fibonacci

def solutie(numar):
    fibo1, fibo2 = 0, 1
    fibo3 = 0
    
    if numar == 1:
        return fibo1
    elif numar == 2:
        return fibo2
    else:
        for i in range(2, numar ):
            fibo3 = fibo1 + fibo2
            fibo1, fibo2 = fibo2, fibo3
    
        return fibo3

if __name__ == "__main__":
    numar = int(input())
    
    print(solutie(numar))