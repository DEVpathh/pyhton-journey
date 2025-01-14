# if __name__ == '__main__':
#     sts_list=[]
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         new_list = [name,score]
#         sts_list.append(new_list)
#     print(sts_list)
#     lowest = float('inf')
#     second_lowest = 0
#     for sts_score in sts_list:
#         if sts_score[1]<lowest:
#             second_lowest=lowest
#             lowest = sts_score[1]

#     print(second_lowest)
        
# Input the number of students
# n = int(input("Enter the number of students: "))

# # Input the student data
# students = []
# for _ in range(n):
#     name = input("Enter student name: ")
#     grade = float(input("Enter student grade: "))
#     students.append([name, grade])

# # Step 1: Extract all grades and find the unique grades
# grades = [student[1] for student in students]
# unique_grades = sorted(set(grades))  # Sort the unique grades

# # Step 2: Find the second lowest grade
# second_lowest_grade = unique_grades[1]

# # Step 3: Find all students with the second lowest grade
# second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

# # Step 4: Sort the names alphabetically
# second_lowest_students.sort()

# for name in second_lowest_students:
#     print(name)

if __name__ == '__main__':
    sts_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sts_list.append([name,score])
    grades = [student[1] for student in sts_list]
    unique_grades = sorted(set(grades))
    second_lowest_grade = unique_grades[1]
    sts_name = [student[0] for student in sts_list if student[1]==second_lowest_grade]
    sts_name.sort()
    for name in sts_name:
        print(name)