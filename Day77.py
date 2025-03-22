#!/bin/python3
import os
from collections import Counter
def equalizeArray(arr):
    freq = Counter(arr)
    max_freq = max(freq.values())
    return len(arr) - max_freq
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
