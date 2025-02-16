from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):  # Loop through each element
        for j in range(i + 1, len(nums)):  # Start from the next element
            if nums[i] + nums[j] == target:  # Check if the sum matches the target
                return [i, j]  # Return the indices as required
    return []  # Return empty list if no solution is found

# Taking input from user
nums = list(map(int, input().rstrip().split()))  # Reading space-separated numbers
target = int(input())  # Reading target value

# Calling the function
print(twoSum(nums, target))
