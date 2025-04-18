#!/bin/python3
import os
def surface_area(grid):
    H = len(grid)
    W = len(grid[0])
    area = 0

    for i in range(H):
        for j in range(W):
            if grid[i][j]:
                area += 2 
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + dx, j + dy
                    neighbor = grid[ni][nj] if 0 <= ni < H and 0 <= nj < W else 0
                    area += max(grid[i][j] - neighbor, 0)                
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
