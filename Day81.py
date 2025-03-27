#!/bin/python3
import os
def organizingContainers(containers):
    n = len(containers)
    container_capacity = [sum(row) for row in containers]
    ball_type_count = [sum(containers[i][j] for i in range(n)) for j in range(n)]
    return "Possible" if sorted(container_capacity) == sorted(ball_type_count) else "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
