#!/bin/python3
def kaprekarNumbers(p, q):
    kaprekar_list = []
    
    for num in range(p, q + 1):
        square = str(num ** 2)
        d = len(str(num))
        
        right_part = square[-d:]
        left_part = square[:-d] if square[:-d] else "0"
        
        if int(left_part) + int(right_part) == num:
            kaprekar_list.append(str(num))
    
    print(" ".join(kaprekar_list) if kaprekar_list else "INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
