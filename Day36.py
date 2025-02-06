# Enter your code here. Read input from STDIN. Print output to STDOUT
def can_stack_cubes(test_cases):
    results = []
    for t in test_cases:
        n, cubes = t
        left, right = 0, n - 1
        top = float('inf')
        possible = True

        while left <= right:
            if cubes[left] <= top and (cubes[left] >= cubes[right] or cubes[right] > top):
                top = cubes[left]
                left += 1
            elif cubes[right] <= top:
                top = cubes[right]
                right -= 1
            else:
                possible = False
                break

        results.append("Yes" if possible else "No")
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    test_cases.append((n, cubes))

results = can_stack_cubes(test_cases)
print("\n".join(results))
