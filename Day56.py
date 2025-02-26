#!/bin/python3
import os
def catAndMouse(x, y, z):
    dist_A = abs(x - z)
    dist_B = abs(y - z)
    if dist_A < dist_B:
        return 'Cat A'
    elif dist_B < dist_A:
        return 'Cat B'
    else:
        return 'Mouse C'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
