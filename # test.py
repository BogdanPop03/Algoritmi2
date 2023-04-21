# test

def Problema4(lista: list) -> list:
    flag = True
    
    while(flag):
        flag = False
        for indice in range(len(lista) - 1):
            if lista[indice] > lista[indice + 1]:
                flag = True
                lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
        
    print(lista)
    
def Problema3_3(numar: int) -> int:
    if numar == 0:
        return 1
    elif numar < 10:
        return 0
    else:
        if numar % 10 == 0:
            return 1 + Problema3_3(numar // 10)
        else:
            return Problema3_3(numar // 10)
    
print(Problema4([4, 3, 2, 1]))

print(Problema3_3(123000321))