def gradingStudents(grades):
    # Write your code here
    up_grad = []
    for marks in grades:
        if marks<38:
            up_grad.append(marks)
        else:
            roundmarks = 5-(marks%5)
            if 0<roundmarks<3:
                up_grad.append(marks+roundmarks)
            else:
                up_grad.append(marks)
    return up_grad


grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
print(gradingStudents(grades))