import hashlib

if __name__ == '__main__':
    n = int(input().strip())  # Read the integer n
    integer_list = map(int, input().strip().split())  # Read the space-separated integers
    tuple_list = tuple(integer_list)  # Convert the list of integers to a tuple
    
    # Convert the tuple to a string or bytes
    tuple_bytes = str(tuple_list).encode()
    
    # Generate a SHA-256 hash
    result = hashlib.sha256(tuple_bytes).hexdigest()
    
    # Convert the hexadecimal string to an integer
    result_int = int(result, 16)
    
    print(result_int)  # Print the integer hash value
