#!/bin/python3
import os
def workbook(n, k, arr):
    special_count = 0
    page = 1
    
    for chapter in range(n):
        num_problems = arr[chapter]
        for problem in range(1, num_problems + 1):
            if problem == page:
                special_count += 1
            if problem % k == 0 or problem == num_problems:
                page += 1
                
    return special_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
