def jimOrders(orders):
    # Write your code here
    my_dict = {}
    for lists in orders:
        my_dict[orders.index(lists)+1]=sum(lists)
    sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
    empty = []
    for keys in sorted_dict:
        empty.append(str(keys))
    return "".join(empty)
n = int(input().strip())

orders = []

for _ in range(n):
    orders.append(list(map(int, input().rstrip().split())))
print(orders)
print(jimOrders(orders))
