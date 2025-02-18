#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    freq = [0] * 101 
    for num in a:
        freq[num] += 1 
    
    max_length = 0
    for i in range(1, 101):
        max_length = max(max_length, freq[i] + freq[i - 1])
    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
