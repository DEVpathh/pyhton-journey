# def plusMinus(arr):
#     positive_score = 0 
#     negative_score = 0
#     zero_score= 0
#     for i in range (0,len(arr)):
#         if arr[i]>0:
#             positive_score += 1
#         elif arr[i]<0:
#             negative_score+= 1
#         else:
#             zero_score += 1
#     tot_posi = positive_score/len(arr)
#     tot_neg = negative_score/len(arr)
#     tot_zero = zero_score/len(arr)

#     round_posi = round(tot_posi,6)
#     round_nega = round(tot_neg,6)
#     round_zero = round(tot_zero,6)
#     print(f"{round_posi:.6f}\n{round_nega:.6f}\n{round_zero:.6f}")




# n = int(input().strip())

# arr = list(map(int, input().rstrip().split()))


# def miniMaxSum(arr):
#     total_sum = 0
#     for i in range(0,len(arr)):
#         total_sum += arr[i]
#     max_sum = 0
#     sum = 0
#     for j in range(0,len(arr)):
#         min_sum = sum
#         sum = total_sum - arr[j]
#         if max_sum < sum:
#             max_sum = sum
#         elif min_sum > sum:
#             min_sum = sum
#     print(f"{min_sum} {max_sum}")


   
   
# if __name__ == '__main__':

#     arr = list(map(int, input().rstrip().split()))

#     miniMaxSum(arr)
if __name__ == '__main__':
    n = int(input())
    for number in range (0,n):
        square = number**2
        print(f"{square}")