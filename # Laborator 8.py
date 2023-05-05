# Laborator 8

# Exemplu 1
def ex1():
    file = open("lab8_1.txt", "a+")
    
    while True:
        input_line = input("Introduceti o linie de text sau \"stop\" pentru a opri citirea: ")
        if input_line == "stop":
            break
        file.write(input_line + '\n')
        
    file.close()
    
    file = open("lab8_1.txt", "r")
        
    print(file.read())
    
    
if __name__ == "__main__":
    ex1()