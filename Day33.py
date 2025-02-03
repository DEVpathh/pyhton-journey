# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
country_stamps = set()
for _ in range(n):
    country = input().strip()
    country_stamps.add(country)
print(len(country_stamps))
