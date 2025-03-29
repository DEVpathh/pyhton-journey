#!/bin/python3
import os
def biggerIsGreater(w):
    w = list(w)
    i = len(w) - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1
    if i == -1:
        return "no answer"
    j = len(w) - 1
    while w[j] <= w[i]:
        j -= 1
    w[i], w[j] = w[j], w[i]
    w = w[:i+1] + w[i+1:][::-1]
    return "".join(w)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
