#!/bin/python3
def countSort(arr):
    n = len(arr)
    result = [[] for _ in range(100)]
    for i in range(n):
        index = int(arr[i][0])
        value = '-' if i < n // 2 else arr[i][1]
        result[index].append(value)
    print(' '.join([val for sublist in result for val in sublist]))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
