from itertools import combinations

N = int(input().strip())
letters = input().strip().split()
k = int(input().strip())

indices_of_a = [i for i, letter in enumerate(letters) if letter == 'a']
all_combinations = list(combinations(range(N), k))
favorable_cases = sum(1 for comb in all_combinations if any(i in indices_of_a for i in comb))

probability = favorable_cases / len(all_combinations)
print(f"{probability:.3f}")
