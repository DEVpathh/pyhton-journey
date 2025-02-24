#!/bin/python3

import math
import os
import random
import re
import sys
def sockMerchant(n, ar):
    sock_counts = {}
    pairs = 0

    for sock in ar:
        if sock in sock_counts:
            sock_counts[sock] += 1
        else:
            sock_counts[sock] = 1

    for count in sock_counts.values():
        pairs += count // 2
    
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
