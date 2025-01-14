def split_and_join(line):
    # write your code here
    splitted_string = []
    word =''
    joined_word = ''
    for each_letter in line:
        if each_letter == ' ':
            splitted_string.append(word)
            word = ''
        else:
            word+=each_letter
    if word:
        splitted_string.append(word)
    for letter in splitted_string:
        if letter != splitted_string[len(splitted_string)-1]:
            joined_word += letter+"-"
        else:
            joined_word+=letter
    return joined_word
            
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)