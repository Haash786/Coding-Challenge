# Import pytest
import pytest

# Import the functions to be tested
from coding_challenge1 import list_binary_n, count_binary_n_without_adj1, create_pattern

""" Tests for the list_binary_n function """

# Test 1: Test if list_binary_n produces binary numbers of length 1
def test_list_binary_1():
    
    # Assert that the result of list_binary_n(1) matches the expected binary numbers
    assert list_binary_n(1) == ['0', '1']

# Test 2: Test if list_binary_n produces binary numbers of length 2
def test_list_binary_2():
    
    # Assert that the result of list_binary_n(2) matches the expected binary numbers
    assert list_binary_n(2) == ['00', '01', '10']

# Test 3: Test if no adjacent 11 in list_binary_n
def test_list_binary_n_11():
    
    # Generate binary numbers for a range of lengths
    for n in range(1, 10):
        binary_numbers = list_binary_n(n)
        
        # Check if there are no adjacent 1s in any of the binary numbers
        for binary_number in binary_numbers:
            assert "11" not in binary_number

""" Tests for the count_binary_n_without_adj1 function """

# Test 4: Test if count_binary_n_without_adj1 handles a non-list input
def test_count_binary_n_without_adj1_non_list():
    
    # Use pytest.raises to check if a TypeError is raised
    with pytest.raises(TypeError):
        
        # Call count_binary_n_without_adj1 with a non-list input "invalid"
        count_binary_n_without_adj1("invalid")

# Test 5: Test if count_binary_n_without_adj1 handles a list with non-string elements
def test_count_binary_n_without_adj1_non_string():
    
    # Use pytest.raises to check if a TypeError is raised
    with pytest.raises(TypeError):
        
        # Call count_binary_n_without_adj1 with a list containing non-string elements
        count_binary_n_without_adj1([1, 2, 3])

# Test 6: Test if count_binary_n_without_adj1 handles an empty list
def test_count_binary_n_without_adj1_empty_list():
    
    # Use pytest.raises to check if an Exception is raised
    with pytest.raises(Exception):
        
        # Call count_binary_n_without_adj1 with an empty list
        count_binary_n_without_adj1([])
    
    
""" Tests for the create_pattern function"""

# Test 7: Test if create_pattern produces a Fibonacci sequence for max_length=12
def test_create_pattern_fibonacci():
    
    # Test with a pattern up to 12 (or any suitable limit)
    result = create_pattern(12)
    
    # Expected Fibonacci sequence
    expected_sequence = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    
    # Convert the pattern dictionary to a list of values
    pattern_values = list(result.values())

    # Check if the pattern values form a Fibonacci sequence
    for i in range(2, len(pattern_values)):
        assert pattern_values[i] == pattern_values[i - 1] + pattern_values[i - 2]

    # Additional checks to ensure the first values match
    assert pattern_values[0] == expected_sequence[0]
    assert pattern_values[1] == expected_sequence[1]

    # This test case ensures that the create_pattern function produces a Fibonacci sequence.
    # It compares the actual pattern values to the expected Fibonacci sequence.
    # If the values match, the test case passes.
    
# Run !pytest for results
