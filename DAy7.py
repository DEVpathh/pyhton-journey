if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if 2<=n<=10:
        for _ in range(n):
            name, *line = input().split()
            
            scores = list(map(float, line))
            if len(scores)==3 and all(0 < score < 100 for score in scores):
                student_marks[name] = scores
            else:
                break
    if len(scores)==3 and all(0 < score < 100 for score in scores):
        query_name = input()
        sum = 0
        for num in student_marks[query_name]:
            sum+=num
        avg = float(sum/3)
        
        
        print(f"{avg:.2f}")
    
