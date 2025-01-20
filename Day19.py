from collections import Counter

# Input data
n = int(input())  # Number of shoes
shoe_sizes = list(map(int, input().split()))  # List of shoe sizes
m = int(input())  # Number of customers

# Inventory count
inventory = Counter(shoe_sizes)

# Total earnings
earnings = 0

# Process each customer
for _ in range(m):
    desired_size, price = map(int, input().split())
    if inventory[desired_size] > 0:
        earnings += price
        inventory[desired_size] -= 1

# Output the total earnings
print(earnings)
