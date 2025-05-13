#!/bin/python3
import os
def pangrams(s):
    s = s.lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in s:
            return "not pangram"
    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
