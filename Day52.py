#!/bin/python3

import math
import os
import random
import re
import sys
def pageCount(n, p):
    from_front = p // 2
    from_back = (n // 2) - (p // 2)
    return min(from_front, from_back)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
