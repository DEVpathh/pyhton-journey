#!/bin/python3
import os
def merge_count(arr):
    if len(arr) < 2:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_count(arr[:mid])
    right, inv_right = merge_count(arr[mid:])
    merged, count = [], 0

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged, inv_left + inv_right + count

def insertionSort(arr):
    _, shifts = merge_count(arr)
    return shifts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
