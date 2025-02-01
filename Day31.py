# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input().strip())
items = OrderedDict()
for _ in range(n):
    *item_name, price = input().split()
    item_name = " ".join(item_name)
    price = int(price)

    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item, net_price in items.items():
    print(item, net_price)
