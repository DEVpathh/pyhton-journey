# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False
#     # Write your logic here
    
#     return leap

# year = int(input())
# print(is_leap(year))
if __name__ == '__main__':
    n = int(input())
    sum = ''
    for i in range(1,n+1):
        character = str(i)
        sum+=character
    
print(sum)