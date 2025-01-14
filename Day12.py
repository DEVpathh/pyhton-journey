# def mutate_string(string, position, character):
#     new_string = string[:position] + character + string[position+1:]
#     return new_string

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)
def count_substring(string, sub_string):
    sub_count = 0
    start = -1
    end = len(sub_string)-2
    for i in range(0,len(string)-len(sub_string)+1):
        if sub_string == string[start+1:end+2]:
            sub_count+=1
        start+=1
        end+=1
  
    return sub_count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)