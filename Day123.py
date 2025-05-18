#!/bin/python3
import os
def countingSort(arr):
    count = [0] * 100
    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(100):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
