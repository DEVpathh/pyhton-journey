#!/bin/python3
import os
def camelcase(s):
    count = 1
    for char in s:
        if char.isupper():
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
