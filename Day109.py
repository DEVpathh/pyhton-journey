#!/bin/python3
def insertionSort1(n, arr):
    value = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(' '.join(map(str, arr)))
        i -= 1
    arr[i + 1] = value
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
