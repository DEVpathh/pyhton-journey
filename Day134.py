#!/bin/python3
import os
def activityNotifications(expenditure, d):
    from bisect import insort, bisect_left

    def get_median(trailing):
        mid = d // 2
        if d % 2 == 0:
            return (trailing[mid - 1] + trailing[mid]) / 2
        else:
            return trailing[mid]

    notifications = 0
    trailing = sorted(expenditure[:d])

    for i in range(d, len(expenditure)):
        median = get_median(trailing)
        if expenditure[i] >= 2 * median:
            notifications += 1

        old_value = expenditure[i - d]
        index = bisect_left(trailing, old_value)
        trailing.pop(index)
        insort(trailing, expenditure[i])

    return notifications

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
