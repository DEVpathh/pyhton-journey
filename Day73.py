def cutTheSticks(arr):
    result = []
    
    while arr:
        result.append(len(arr))
        min_stick = min(arr)
        arr = [x - min_stick for x in arr if x > min_stick]
    
    return result
