#!/bin/python3
import os
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    count = 0
    if not any(char in numbers for char in password):
        count += 1
    if not any(char in lower_case for char in password):
        count += 1
    if not any(char in upper_case for char in password):
        count += 1
    if not any(char in special_characters for char in password):
        count += 1

    return max(count, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
