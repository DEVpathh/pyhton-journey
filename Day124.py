#!/bin/python3
import os
def gemstones(arr):
    common = set(arr[0])
    for rock in arr[1:]:
        common &= set(rock)
    return len(common)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
