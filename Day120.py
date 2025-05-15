#!/bin/python3
def separateNumbers(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        first = int(s[:i])
        current = first
        temp = ''
        while len(temp) < n:
            temp += str(current)
            current += 1
        if temp == s:
            print("YES", first)
            return
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
