#!/bin/python3
import os
def lilysHomework(arr):
    def min_swaps(to_sort):
        n = len(to_sort)
        arrpos = list(enumerate(to_sort))
        arrpos.sort(key=lambda x: x[1])
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arrpos[i][0] == i:
                continue
            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arrpos[j][0]
                cycle_size += 1
            if cycle_size > 0:
                swaps += cycle_size - 1
        return swaps

    return min(min_swaps(arr), min_swaps(arr[::-1]))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
