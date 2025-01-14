if __name__ == '__main__':
    N = int(input())
    commands = [] 
    empty_list = []

    for _ in range(N):
        commands.append(input().split()) 

    for user_input in commands:
        command = user_input[0]

        if command == 'insert':
            index = int(user_input[1])
            element = int(user_input[2])
            empty_list.insert(index, element)
        elif command == 'print':
            print(empty_list)
        elif command == 'remove':
            element = int(user_input[1])
            empty_list.remove(element)
        elif command == 'append':
            element = int(user_input[1])
            empty_list.append(element)
        elif command == 'sort':
            empty_list.sort()
        elif command == 'pop':
            empty_list.pop()
        elif command == 'reverse':
            empty_list.reverse()



