#!/bin/python3
import os
def strangeCounter(t):
    cycle_start = 1
    value = 3
    
    while t > cycle_start + value - 1:
        cycle_start += value
        value *= 2
    
    return value - (t - cycle_start)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
