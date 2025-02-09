def plusMinus(arr):
    # Write your code here
    pos = 0 
    neg = 0
    zero = 0
    for i in arr:
        if i == abs(i) and i != 0:
            pos += 1
        elif i == 0 :
            zero+=1
        else: 
            neg += 1
    ratio_pos = pos/len(arr)
    ratio_neg = neg/len(arr)
    ratio_zero = zero/len(arr)
    print(f"{ratio_pos:.6f}\n{ratio_neg:.6f}\n{ratio_zero:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
