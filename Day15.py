

# Complete the solve function below.
def solve(s):
    list_s = s.split(' ')
    new_s = ''
    i = 0
    print(list_s)
    for char in list_s:
        new_s += char.capitalize()+' '
    return new_s
sting = input()

print(solve(sting))