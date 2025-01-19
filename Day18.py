from itertools import product

# Input and conversion to integers
A = input().split()
converted_A = [int(x) for x in A]
B = input().split()
converted_B = [int(y) for y in B]

# Generating the Cartesian product
result = list(product(converted_A, converted_B))

# Formatting the output as a space-separated string
cartesian_product = " ".join(str(pair) for pair in result)
print(cartesian_product)

