#!/bin/python3
import os
from itertools import combinations
def alternate(s):
    unique_chars = set(s)
    max_length = 0
    for ch1, ch2 in combinations(unique_chars, 2):
        filtered = [c for c in s if c == ch1 or c == ch2]
        if all(filtered[i] != filtered[i+1] for i in range(len(filtered) - 1)):
            max_length = max(max_length, len(filtered))
    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
