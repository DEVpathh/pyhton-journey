#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diag1_sum = 0
    diag2_sum = 0
    i = 0
    j = 0 
    k = len(arr)-1
    while i < len(arr):
        diag1_sum += arr[i][j]
        diag2_sum += arr[i][k]
        i+= 1
        j+= 1
        k-= 1
    diff = abs(diag1_sum - diag2_sum)

    return diff 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
