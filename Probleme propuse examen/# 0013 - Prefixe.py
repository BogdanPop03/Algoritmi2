# 0013 - Prefixe

def validareDate(text):
    try:
        if len(text) > 10:
            raise ValueError("Text length should be at most 10.")

        if not text.islower():
            raise ValueError("Text should consist only of lowercase letters.")

        print("Valid input:", text)
        
        return text

    except ValueError as e:
        print("Invalid input:", str(e))
        return

def solutie(text):
    for indice in reversed(range(len(text))):
        print(text[:indice])
    for indice in range(len(text)):
        print(text[indice:])

if __name__ == "__main__":
    text = input()
    
    text = validareDate(text)
    
    if text is not None:
        solutie(text)