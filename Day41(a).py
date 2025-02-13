def timeConversion(s):
    hour = int(s[0:2])
    min = s[3:5]
    sec = s[6:8]
    if 'AM' in s or'am' in s:
        if hour == 12:
            hour = "00"
    elif 'PM' in s or'pm' in s:

        if hour == 12:
            hour = 12
        else:
            hour+=12
    print(f"{hour}:{min}:{sec}")
s = input()
timeConversion(s)