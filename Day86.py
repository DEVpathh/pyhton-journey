#!/bin/python3
import os
def minimumDistances(a):
    index_map = {}
    min_distance = float('inf')

    for i, value in enumerate(a):
        if value in index_map:
            min_distance = min(min_distance, i - index_map[value])
        index_map[value] = i

    return min_distance if min_distance != float('inf') else -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
