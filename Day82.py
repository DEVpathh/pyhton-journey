#!/bin/python3
import os
import math
def encryption(s):
    s = s.replace(" ", "")
    n = len(s)
    rows = math.floor(math.sqrt(n))
    cols = math.ceil(math.sqrt(n))
    if rows * cols < n:
        rows += 1
    grid = [s[i:i+cols] for i in range(0, n, cols)]
    encrypted_text = []
    for i in range(cols):
        encrypted_text.append("".join(row[i] for row in grid if i < len(row)))
    return " ".join(encrypted_text)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
