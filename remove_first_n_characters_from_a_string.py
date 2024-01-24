# Write a program to remove characters from a string starting from zero up to n and return a new string.

# Example 
# string:"pynative"
# number to remove: 4

def remove_first_n_chars(input_string, number):
    return input_string[number:]

user_input = input("Enter a string: ")
number_to_remove = int(input("Enter the number of characters to remove: "))

result_string = remove_first_n_chars(user_input, number_to_remove)
print(f"New string: {result_string}")
