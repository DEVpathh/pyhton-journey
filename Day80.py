#!/bin/python3
import os
def taumBday(b, w, bc, wc, z):
    cost1 = b * bc + w * wc
    cost2 = b * (wc + z) + w * wc
    cost3 = b * bc + w * (bc + z)
    return min(cost1, cost2, cost3)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
