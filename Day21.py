# Enter your code here. Read input from STDIN. Print output to STDOUT\
from itertools import permutations
input_string, k = input().split()
k = int(k)

sorted_string = sorted(input_string)

permutation_list = permutations(sorted_string, k)

for p in permutation_list:
    print(''.join(p))
