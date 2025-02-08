#!/bin/python3
import os
def compareTriplets(a, b):
    # Write your code here
    a_score = 0
    b_score = 0
    for i in range(len(a)):
        if  a[i]>b[i]:
            a_score+=1
        if a[i]<b[i]:
            b_score+=1
        else:
            a_score+=0
            b_score+=0
    res_list = []
    res_list.extend([a_score,b_score])
    return res_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
