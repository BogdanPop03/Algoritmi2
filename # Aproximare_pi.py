# Aproximare_pi

import random
import math

def isInsideTheCircle(coord_x: float, coord_y: float) -> bool:
    if math.sqrt((coord_x - 1) ** 2 + (coord_y - 1) ** 2) <= 1:
        return True
    
    return False

inside_the_circle: int = int(0)
inside_the_square: int = int(0)

for count in range(2_000_000):
    coord_x: float = random.uniform(0, 2)
    coord_y: float = random.uniform(0, 2)
    
    if isInsideTheCircle(coord_x, coord_y):
        inside_the_circle += 1
    
    inside_the_square += 1
    

pi: float = 4 * inside_the_circle / inside_the_square

print(f'The aproximate value of pi is: {pi}')