# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     coordinates = [
#     [i, j, k]
#     for i in range(x + 1)
#     for j in range(y + 1)
#     for k in range(z + 1)
#     if i + j + k != n
# ]

#     print(coordinates)
if __name__ == '__main__':
    n = int(input())  
    arr = map(int, input().split()) 
    scores = list(arr)
    max_score = -101  
    runner_up_score = -101 

    
    if all(-100 <= score <= 100 for score in scores):
        if n >= 2 and n <= 10:
            scores = sorted(set(scores), reverse=True)
            if len(scores) > 1:
                runner_up_score = scores[1]
            else:
                runner_up_score = max_score 

        print(runner_up_score) 
    


