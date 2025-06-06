#!/bin/python3
import os
from collections import Counter

def isValid(s):
    char_freq = Counter(s)
    freq_count = Counter(char_freq.values())
    
    if len(freq_count) == 1:
        return "YES"
    
    if len(freq_count) == 2:
        keys = list(freq_count.keys())
        val1, val2 = keys[0], keys[1]
        if (freq_count[val1] == 1 and (val1 - 1 == val2 or val1 == 1)) or \
           (freq_count[val2] == 1 and (val2 - 1 == val1 or val2 == 1)):
            return "YES"
    
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
