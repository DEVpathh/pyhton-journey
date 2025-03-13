#!/bin/python3
def extraLongFactorials(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)
if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
