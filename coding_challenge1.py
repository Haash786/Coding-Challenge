### Coding Challenge 1 ### 

# Binary numbers are made of only 0 and 1.
# How many n-digit binary numbers are there that don't have two adjacent 1 bits?

""" 1 - Make a function
	Inputs: Positive integer
	Returns: List of strings of all binary numbers of that length """
    
# Define a function that generates binary numbers of a specified length 'n' without adjacent 1 bits
def list_binary_n(n):
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

""" 2 - Make a function
	Inputs: List of strings
	Returns: Integer (all binary numbers in the input which have no neighbouring 1 bits) """

# Define a function that counts the number of binary numbers without adjacent 1 bits in a list
def count_binary_n_without_adj1(binary_n):
    count = 0
    for num in binary_n:
        # Create marker to see if there are two 1s next to each other in the binary string
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

# Define a function that generates a pattern of counts for binary numbers of different lengths
def create_pattern(max_length):
    pattern = {}
    for n in range(1, max_length + 1):
        # Generate binary numbers of length 'n'
        binary_n = list_binary_n(n)
        # Calculate the count of binary numbers without adjacent 1s by calling the function
        count = count_binary_n_without_adj1(binary_n)
        # Store the count in the pattern dictionary with the key 'n'
        pattern[n] = count

    return pattern

""" 3 - Make a table / dictionary / print function / other logical structure of your choice
	Column 1: Number of digits
	Column 2: Count of binary numbers that don't have neighbouring 1 bits """

# Define a function to print the pattern in a formatted table
def print_pattern(pattern):
    print("Number of Digits | Count of Binary Numbers Without Adjacent 1s")
    for n, count in pattern.items():
        # Format and print the pattern with the number of digits and the count
        print(f"{n:16} | {count:40}")
        
# Example usage:
max_length = 15
pattern = create_pattern(max_length)
print_pattern(pattern)

""" 4/5 - Work out the pattern in words & explain/justify why the pattern exists """

# Pattern is similar to the fibinocci sequence as with each new digit added the choices are determined by the ending digit of the existing number.
# The pattern is the way it is because when adding a new digit to the end of a binary number (without repeating 1s) there are only two possibilities:
# If the last digit is 0, you can add either 0 or 1
# If the last digit is 1, you can only add 1
# Therefor Fn = F(n-1) + F(n-2)