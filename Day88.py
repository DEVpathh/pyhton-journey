#!/bin/python3
import os
def timeInWords(h, m):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]
    if m == 0:
        return f"{words[h]} o' clock"
    elif m == 15 or m == 30:
        return f"{words[m]} past {words[h]}"
    elif m == 45:
        return f"{words[15]} to {words[h+1]}"
    elif m == 1:
        return f"one minute past {words[h]}"
    elif m < 30:
        return f"{words[m]} minutes past {words[h]}"
    elif m == 59:
        return f"one minute to {words[h+1]}"
    else:
        return f"{words[60-m]} minutes to {words[h+1]}"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
