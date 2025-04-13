#!/bin/python3
import os
def stones(n, a, b):
    result = set()
    for i in range(n):
        value = i * a + (n - 1 - i) * b
        result.add(value)
    return sorted(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
