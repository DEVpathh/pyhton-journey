#!/bin/python3
import os
def beautifulBinaryString(b):
    count = 0
    i = 0
    while i <= len(b) - 3:
        if b[i:i+3] == '010':
            count += 1
            i += 3
        else:
            i += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
