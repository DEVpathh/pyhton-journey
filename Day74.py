#!/bin/python3
import os
def nonDivisibleSubset(k, S):
    remainder_counts = [0] * k
    for num in S:
        remainder_counts[num % k] += 1

    max_subset_size = min(remainder_counts[0], 1)

    for r in range(1, (k // 2) + 1):
        if r == k - r:
            max_subset_size += min(remainder_counts[r], 1)
        else:
            max_subset_size += max(remainder_counts[r], remainder_counts[k - r])

    return max_subset_size
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
