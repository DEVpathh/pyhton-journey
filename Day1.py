import random
s = input("enter a company name\n")

randomised_name = ''.join(random.sample(s,len(s)))


distinct_char = randomised_name[0]
count = 0
count_char = {}
def character_counter(name):
    for char in name:
        if char in count_char:
            count_char[char]+=1
        else:
            count_char[char]=1
    return count_char
for letter in randomised_name:
    if distinct_char != letter:
        count+=1
if count < 3:
    pass
else:
    wow = character_counter(randomised_name)
    sorted_dict = sorted(wow.items(), key = lambda item: (-item[1], item[0])) 
    for i in range (3):
        key,value = sorted_dict[i]
        print(f"{key} {value}")







