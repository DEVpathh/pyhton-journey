#!/bin/python3
import os
def jumpingOnClouds(c):
    jumps = 0
    position = 0
    n = len(c)

    while position < n - 1:
        if position + 2 < n and c[position + 2] == 0:
            position += 2
        else:
            position += 1
        jumps += 1

    return jumps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
