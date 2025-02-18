#!/bin/python3

import math
import os
import random
import re
import sys
def climbingLeaderboard(ranked, player):
    unique_ranks = sorted(set(ranked), reverse=True)  
    results = []
    index = len(unique_ranks)  
    
    for score in player:
        while index > 0 and score >= unique_ranks[index - 1]:  
            index -= 1
        results.append(index + 1) 
    
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
