#!/bin/python3
import os
def caesarCipher(s, k):
    result = ''
    k = k % 26
    for char in s:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + k) % 26 + base)
            result += shifted
        else:
            result += char
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
