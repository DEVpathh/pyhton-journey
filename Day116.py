#!/bin/python3
import os
def hackerrankInString(s):
    target = "hackerrank"
    i = 0
    for char in s:
        if i < len(target) and char == target[i]:
            i += 1
    return "YES" if i == len(target) else "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
