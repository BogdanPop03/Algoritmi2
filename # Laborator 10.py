# Laborator 10

graph = [[0, 1], [0, 2],
         [1, 2], [1, 3],
         [2, 4], [2, 6],
         [4, 5],
         [5, 7]]

noduri_parcurse = []
flag = False

def parcurgereGraph(graph, start, noduri_parcurse, flag):
    if start in noduri_parcurse:
        flag = True
    if flag == False:
        for element in graph:
            if element[0] == start and start not in noduri_parcurse:
                noduri_parcurse.append(start)
                # print(noduri_parcurse, noduri_parcurse.count(start))
                parcurgereGraph(graph, element[1], noduri_parcurse, flag)
        if noduri_parcurse.count(start) == 0:
            noduri_parcurse.append(start)
            
    '''
    curent_n = start
    for element in graph:
        if element[0] == curent_n:
            noduri_parcurse.append(element[0])
            curent_n = element[1]
    noduri_parcurse.append(element[0])
    '''
        

if __name__ == "__main__":
    parcurgereGraph(graph, 0, noduri_parcurse, flag)
    
    print(noduri_parcurse)
    