#!/bin/python3

import math
import os
import sys

# Function to calculate LCM of two numbers
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

# Function to calculate LCM of an array
def find_lcm(arr):
    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)
    return result

# Function to calculate GCD of an array
def find_gcd(arr):
    result = arr[0]
    for num in arr[1:]:
        result = math.gcd(result, num)
    return result

# Function to find the total count of numbers between the sets
def getTotalX(a, b):
    lcm_a = find_lcm(a)  # LCM of first array
    gcd_b = find_gcd(b)  # GCD of second array

    count = 0
    multiple = lcm_a

    while multiple <= gcd_b:
        if gcd_b % multiple == 0:  # Check if it's a factor of GCD
            count += 1
        multiple += lcm_a  # Move to next multiple of LCM
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
