#!/bin/python3
import os
def gameOfThrones(s):
    from collections import Counter
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)
    if odd_count > 1:
        return "NO"
    else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
