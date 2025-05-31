#!/bin/python3
import os
def makingAnagrams(s1, s2):
    from collections import Counter
    
    freq1 = Counter(s1)
    freq2 = Counter(s2)
    
    deletions = 0
    for char in set(freq1.keys()).union(freq2.keys()):
        deletions += abs(freq1.get(char, 0) - freq2.get(char, 0))
    
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
