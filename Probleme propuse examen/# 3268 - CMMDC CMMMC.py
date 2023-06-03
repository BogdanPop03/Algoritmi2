# 3268 - CMMDC CMMMC

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
    
    
    return cmmdc, cmmmc

if __name__ == "__main__":
    numar1 = int(input())
    numar2 = int(input())
    
    print(solutie(numar1, numar2))