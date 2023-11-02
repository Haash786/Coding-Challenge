### Coding Challenge 1 ###

# Binary numbers are made of only 0 and 1.
# How many n-digit binary numbers are there that don't have two adjacent 1 bits?

""" 
1 - Generate a list of binary numbers of a specified length without adjacent 1 bits
    
    Inputs:
        n (int): The length of binary numbers to generate.
    Returns:
        list of str: A list of binary numbers without adjacent 1 bits.
    Raises:
        TypeError: If n is not an integer.
        Exception: If n is not a positive integer.
"""

def list_binary_n(n):
    if not isinstance(n, int):
        raise TypeError("n should be an integer.")
    if n <= 0:
        raise Exception("n should be a positive integer.")

    # Define an inner function that generates binary strings
    def list_binary_str(n, s=""):
        # If n is 0, return a list containing the current binary string 's'
        if n == 0:
            return [s]
        else:
            strings = []
            # Generate binary strings by adding "0" to the end
            strings.extend(list_binary_str(n - 1, s + "0"))
            # Check if the last character is not "1" before adding "1" to avoid adjacent 1s
            if s == "" or s[-1] != "1":
                strings.extend(list_binary_str(n - 1, s + "1"))
            return strings

    return list_binary_str(n)

""" 
2 - Count the number of binary numbers without adjacent 1 bits in a list
    
    Inputs:
        binary_n (list of str): A list of binary numbers.
    Returns:
        int: The count of binary numbers without adjacent 1 bits.
    Raises:
        TypeError: If binary_n is not a list or its elements are not strings.
        Exception: If binary_n is an empty list.
"""

def count_binary_n_without_adj1(binary_n):
    if not isinstance(binary_n, list):
        raise TypeError("binary_n should be a list.")
    if not all(isinstance(num, str) for num in binary_n):
        raise TypeError("Elements of binary_n should be strings.")
    if len(binary_n) == 0:
        raise Exception("binary_n should not be an empty list.")

    count = 0
    for num in binary_n:
        # Create a marker to see if there are two 1s next to each other in the binary string
        has_adj1 = False
        for i in range(len(num) - 1):
            # Check for "11" (adjacent 1s) in the binary string
            if num[i:i+2] == "11":
                has_adj1 = True
                break
        # If there are no adjacent 1s, add 1 to the count
        if not has_adj1:
            count += 1
            
    return count

""" 
3 - Generate a pattern of counts for binary numbers of different lengths
    
    Inputs:
        max_length (int): The maximum length of binary numbers to consider.
    Returns:
        dict: A dictionary containing the counts of binary numbers without adjacent 1 bits for different lengths.
    Raises:
        TypeError: If max_length is not an integer.
        Exception: If max_length is not a positive integer.
"""

def create_pattern(max_length):
    if not isinstance(max_length, int):
        raise TypeError("max_length should be an integer.")
    if max_length <= 0:
        raise Exception("max_length should be a positive integer.")

    pattern = {}
    for n in range(1, max_length + 1):
        # Generate binary numbers of length 'n'
        binary_n = list_binary_n(n)
        # Calculate the count of binary numbers without adjacent 1s by calling the function
        count = count_binary_n_without_adj1(binary_n)
        # Store the count in the pattern dictionary with the key 'n'
        pattern[n] = count

    return pattern

""" 
4 - Print the pattern of counts in a formatted table
    
    Inputs:
        pattern (dict): A dictionary containing the counts of binary numbers without adjacent 1 bits for different lengths.
    Returns:
        None
    Raises:
        TypeError: If pattern is not a dictionary.
        Exception: If pattern is an empty dictionary.
"""

def print_pattern(pattern):
    if not isinstance(pattern, dict):
        raise TypeError("pattern should be a dictionary.")
    if not pattern:
        raise Exception("pattern should not be an empty dictionary.")

    print("Number of Digits | Count of Binary Numbers Without Adjacent 1s")
    for n, count in pattern.items():
        # Format and print the pattern with the number of digits and the count
        print(f"{n:16} | {count:40}")

# Example usage:
max_length = 15
pattern = create_pattern(max_length)
print_pattern(pattern)

""" 
5 - Explain the pattern of binary numbers without adjacent 1 bits
The pattern is similar to the Fibonacci sequence as with each new digit added the choices are determined by the ending digit of the existing number.
The pattern is the way it is because when adding a new digit to the end of a binary number (without repeating 1s) there are only two possibilities:
    - If the last digit is 0, you can add either 0 or 1.
    - If the last digit is 1, you can only add 1.
Therefore, Fn = F(n-1) + F(n-2)
"""
