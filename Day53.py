#!/bin/python3
import os
def countingValleys(steps, path):
    altitude = 0 
    valleys = 0
    for step in path:
        if step == 'U':
            altitude += 1
        else:  # step == 'D'
            altitude -= 1
        if step == 'U' and altitude == 0:
            valleys += 1    
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
