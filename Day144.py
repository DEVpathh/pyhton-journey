#!/bin/python3
import os
from collections import defaultdict

def sherlockAndAnagrams(s):
    substr_freq = defaultdict(int)
    
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            signature = ''.join(sorted(substr))
            substr_freq[signature] += 1

    count = 0
    for freq in substr_freq.values():
        if freq > 1:
            count += (freq * (freq - 1)) // 2
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = sherlockAndAnagrams(s)
        fptr.write(str(result) + '\n')

    fptr.close()
