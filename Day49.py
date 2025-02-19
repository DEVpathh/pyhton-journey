#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

def migratoryBirds(arr):
    bird_counts = Counter(arr)
    max_count = max(bird_counts.values())
    most_common_birds = [bird for bird, count in bird_counts.items() if count == max_count]
    return min(most_common_birds) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
