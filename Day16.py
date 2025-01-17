def merge_the_tools(string, k):
    # your code goes here
    sub_str = ''
    rep_str = ''
    start = 0
    end = k
    while(start<len(string)):
        sub_str += string[start:end]+' '
        start += k
        end += k
    splitted_sub_str = sub_str.split()
    
    for char in splitted_sub_str:
        empty_list = []
        list_of_char = list(char)
        for i in list_of_char:
            if i not in empty_list:
                empty_list.append(i)
        print(''.join(empty_list))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
