#!/bin/python3
def almostSorted(arr):
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        print("yes")
        return

    n = len(arr)
    diff = [i for i in range(n) if arr[i] != sorted_arr[i]]

    if len(diff) == 2:
        print("yes")
        print(f"swap {diff[0] + 1} {diff[1] + 1}")
    else:
        l, r = diff[0], diff[-1]
        if arr[l:r + 1] == sorted_arr[l:r + 1][::-1]:
            print("yes")
            print(f"reverse {l + 1} {r + 1}")
        else:
            print("no")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
