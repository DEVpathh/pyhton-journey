#!/bin/python3
import os
def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100 
    i = 0    
    while True:
        i = (i + k) % n
        energy -= 1 + 2 * c[i]
        if i == 0:
            break
    return energy
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
