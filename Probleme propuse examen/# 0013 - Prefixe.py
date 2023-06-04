# 0013 - Prefixe

def solutie(text):
    for indice in reversed(range(len(text))):
        print(text[:indice])
    for indice in range(len(text)):
        print(text[indice:])

if __name__ == "__main__":
    text = input()
    
    solutie(text)