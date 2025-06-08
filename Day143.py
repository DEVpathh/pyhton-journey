#!/bin/python3

import math
import os
import random
import re
import sys

MOD = 10**9 + 7
prefix = []
fact = []
invfact = []
def modinv(a, p):
    return pow(a, p - 2, p)
def precompute_factorials(n, MOD):
    fact = [1] * (n + 1)
    invfact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    invfact[n] = modinv(fact[n], MOD)
    for i in range(n - 1, -1, -1):
        invfact[i] = invfact[i + 1] * (i + 1) % MOD
    return fact, invfact
def initialize(s):
    global prefix, fact, invfact
    n = len(s)
    prefix = [[0] * 26 for _ in range(n + 1)]
    for i in range(n):
        for j in range(26):
            prefix[i + 1][j] = prefix[i][j]
        prefix[i + 1][ord(s[i]) - ord('a')] += 1
    
    fact, invfact = precompute_factorials(n, MOD)
def answerQuery(l, r):
    global prefix, fact, invfact
    freq = [0] * 26
    for i in range(26):
        freq[i] = prefix[r][i] - prefix[l - 1][i]

    half_counts = [f // 2 for f in freq]
    pair_sum = sum(half_counts)

    numerator = fact[pair_sum]
    denominator = 1
    for hc in half_counts:
        if hc > 0:
            denominator = denominator * fact[hc] % MOD

    ways = numerator * modinv(denominator, MOD) % MOD

    odd_count = sum(f % 2 for f in freq)
    if odd_count == 0:
        center_choices = 1
    else:
        center_choices = odd_count

    return ways * center_choices % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()
    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        l = int(first_multiple_input[0])
        r = int(first_multiple_input[1])
        result = answerQuery(l, r)
        fptr.write(str(result) + '\n')

    fptr.close()
