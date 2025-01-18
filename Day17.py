from __future__ import print_function
str_input = input()
operation = str_input[5:]

if "print" in str_input:
    print(eval(operation))
    