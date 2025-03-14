#!/bin/python3
import os
def appendAndDelete(s, t, k):
    common_length = 0
    while common_length < len(s) and common_length < len(t) and s[common_length] == t[common_length]:
        common_length += 1

    total_operations = len(s) - common_length + len(t) - common_length

    if total_operations <= k and (k - total_operations) % 2 == 0:
        return "Yes"
    elif len(s) + len(t) <= k:
        return "Yes"
    else:
        return "No"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
