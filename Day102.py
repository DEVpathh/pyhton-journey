#!/bin/python3
import os

def twoPluses(grid):
    n, m = len(grid), len(grid[0])

    up = [[0]*m for _ in range(n)]
    down = [[0]*m for _ in range(n)]
    left = [[0]*m for _ in range(n)]
    right = [[0]*m for _ in range(n)]

    # Precompute up and left
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'G':
                up[i][j] = up[i-1][j] + 1 if i > 0 else 1
                left[i][j] = left[i][j-1] + 1 if j > 0 else 1

    # Precompute down and right
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            if grid[i][j] == 'G':
                if i < n - 1:
                    down[i][j] = down[i+1][j] + 1
                else:
                    down[i][j] = 1
                if j < m - 1:
                    right[i][j] = right[i][j+1] + 1
                else:
                    right[i][j] = 1

    pluses = []

    for i in range(n):
        for j in range(m):
            max_arm = min(up[i][j], down[i][j], left[i][j], right[i][j])
            for k in range(max_arm):
                area = 4 * k + 1
                cells = set([(i, j)])
                for d in range(1, k + 1):
                    cells.update([(i - d, j), (i + d, j), (i, j - d), (i, j + d)])
                pluses.append((area, cells))

    max_product = 0
    for i in range(len(pluses)):
        for j in range(i + 1, len(pluses)):
            area1, c1 = pluses[i]
            area2, c2 = pluses[j]
            if c1.isdisjoint(c2):
                max_product = max(max_product, area1 * area2)

    return max_product


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
