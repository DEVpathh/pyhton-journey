if __name__ == '__main__':
    s = input()

    # Check for alphanumeric characters
    print(any(char.isalnum() for char in s))
    
    # Check for alphabetical characters
    print(any(char.isalpha() for char in s))
    
    # Check for digits
    print(any(char.isdigit() for char in s))
    
    # Check for lowercase characters
    print(any(char.islower() for char in s))
    
    # Check for uppercase characters
    print(any(char.isupper() for char in s))
     

        
