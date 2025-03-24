#!/bin/python3
import os
from itertools import combinations
def acmTeam(topic):
    max_topics = 0
    team_count = 0
    
    for team in combinations(topic, 2):
        topics_known = bin(int(team[0], 2) | int(team[1], 2)).count('1')
        
        if topics_known > max_topics:
            max_topics = topics_known
            team_count = 1
        elif topics_known == max_topics:
            team_count += 1
    
    return [max_topics, team_count]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
