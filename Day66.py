#!/bin/python3

import os

def permutationEquation(p):
    value_to_index = {value: index + 1 for index, value in enumerate(p)}
    return [value_to_index[value_to_index[x]] for x in range(1, len(p) + 1)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
