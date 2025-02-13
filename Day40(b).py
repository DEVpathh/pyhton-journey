
def max_num(arr):
    max_sum = 0 
    min_sum = float('inf')
    i = 0
    result = []
    while i<len(arr):
        sum = 0
        for num in arr:
            if num != arr[i]:
                sum+=num
            if sum > max_sum:
                max_sum = sum
        if sum<min_sum:
            min_sum = sum
        i+= 1
    result=f"{min_sum} {max_sum}"
    
    return result
    

print(max_num([5,5,5,5,5]))
