# Curs_Data_8_05_2023

import random
import math

# Aproximare pi
def aproximarePi():
    def isInsideTheCircle(coord_x: float, coord_y: float) -> bool:
        if math.sqrt((coord_x - 1) ** 2 + (coord_y - 1) ** 2) <= 1:
            return True
        return False

    inside_the_circle: int = int(0)
    inside_the_square: int = int(0)

    for count in range(2_500_000):
        coord_x: float = random.uniform(0, 2)
        coord_y: float = random.uniform(0, 2)
        
        if isInsideTheCircle(coord_x, coord_y):
            inside_the_circle += 1
        
        inside_the_square += 1
        

    pi: float = 4 * inside_the_circle / inside_the_square

    print(f'The aproximate value of pi is: {pi}')

import heapq

def comisVoiajor():
    matrix = []
    
    with open("comis_voiajor_in.txt" , "r") as file_in:
        for line in file_in:
            values = line.split()
            matrix.append([float(value) for value in values])
            
    file_in.close()
    
    # print(matrix)
    
    start = 0
    end = 11
    
    distance = {i: float('inf') for i in range(len(matrix))}
    distance[start] = 0

    # Initialize the path dictionary with empty paths for all nodes
    path = {i: [] for i in range(len(matrix))}
    path[start] = [start]

    # Initialize the heap with the starting node and its distance
    heap = [(0, start)]

    # Initialize the visited set
    visited = set()

    # While there are still nodes to visit
    while heap:
        # Pop the node with the smallest distance from the heap
        (dist, node) = heapq.heappop(heap)

        # If we've already visited this node, skip it
        if node in visited:
            continue

        # Otherwise, mark it as visited
        visited.add(node)

        # Update the distances and paths of all neighboring nodes
        for neighbor, weight in enumerate(matrix[node]):
            if weight == 0:
                continue
            new_distance = dist + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                path[neighbor] = path[node] + [neighbor]
                heapq.heappush(heap, (new_distance, neighbor))

    # Return the shortest path from the starting node to the end node
    return path[end]
    

if __name__ == "__main__":
    # aproximarePi()
    
    print(comisVoiajor())