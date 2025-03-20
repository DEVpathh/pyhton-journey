#!/bin/python3
import os
def repeatedString(s, n):
    count_a_in_s = s.count('a')
    full_repeats = n // len(s)
    remaining_chars = n % len(s)
    count_a_in_remaining = s[:remaining_chars].count('a')
    return count_a_in_s * full_repeats + count_a_in_remaining
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
