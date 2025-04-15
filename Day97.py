#!/bin/python3
import os
def happyLadybugs(b):
    from collections import Counter

    if "_" in b:
        counts = Counter(b)
        for k, v in counts.items():
            if k != "_" and v < 2:
                return "NO"
        return "YES"
    else:
        n = len(b)
        for i in range(n):
            if (i > 0 and b[i] == b[i - 1]) or (i < n - 1 and b[i] == b[i + 1]):
                continue
            else:
                return "NO"
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
