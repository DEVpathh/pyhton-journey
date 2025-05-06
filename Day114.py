#!/bin/python3
import os
def marsExploration(s):
    expected = 'SOS' * (len(s) // 3)
    return sum(1 for a, b in zip(s, expected) if a != b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
