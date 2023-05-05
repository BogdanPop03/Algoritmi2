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
        
    print(file.read(), end = "")
    

def ex2():
    file = open("lab8_2.txt", "r")
    
    linie1 = file.readline().strip().split(" ")
    
    nr_linii = int(linie1[0])
    nr_coloane = int(linie1[1])
    
    matrice = []
    
    for linie in range(nr_linii):
        aux = file.readline().strip().split(" ")
        aux = list(map(int, aux))
        matrice.append(aux)
    
    file.close()
        
    file = open("lab8_1.txt", "a")
    
    file.writelines(str(matrice))
    
    file.close()
    
    file = open("lab8_1.txt", "r")
    
    print(file.read(), end = "")
    
    
if __name__ == "__main__":
    print("ex1: ")
    ex1()
    print("\nex2: ")
    ex2()