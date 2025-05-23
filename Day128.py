#!/bin/python3
import os
def theLoveLetterMystery(s):
    operations = 0
    n = len(s)
    for i in range(n // 2):
        operations += abs(ord(s[i]) - ord(s[n - 1 - i]))
    return operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
