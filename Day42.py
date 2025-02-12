def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    noOfOranges = 0
    noOfApples = 0
    for i in apples:
        if s<=(a + i)<=t:
            noOfApples += 1
    for j in oranges:
        if s<=(b+j)<=t:
            noOfOranges+=1

    print(f"{noOfApples} \n{noOfOranges}")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)