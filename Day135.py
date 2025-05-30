#!/bin/python3
import os
def anagram(s):
    if len(s) % 2 != 0:
        return -1
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    freq1 = [0] * 26
    freq2 = [0] * 26
    for c in s1:
        freq1[ord(c) - ord('a')] += 1
    for c in s2:
        freq2[ord(c) - ord('a')] += 1
    changes = 0
    for i in range(26):
        if freq1[i] > freq2[i]:
            changes += freq1[i] - freq2[i]
    return changes
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
