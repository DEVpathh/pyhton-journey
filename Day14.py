# def door_mat():
#     # Taking input for N and M
#     n, m = map(int, input().split())
    
#     # Validate the inputs
#     if n % 2 != 0 and m== 3 * n:

#         for i in range(1, n, 2):
#             pattern = (".|." * i).center(m, "-")
#             print(pattern)

#         print("WELCOME".center(m, "-"))

#         for i in range(n-2, 0, -2):
#             pattern = (".|." * i).center(m, "-")
#             print(pattern)

# door_mat()
def print_formatted(number):
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        
        print(f"{str(i).rjust(width)} {oct(i)[2:].rjust(width)} {hex(i)[2:].upper().rjust(width)} {bin(i)[2:].rjust(width)}")



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
