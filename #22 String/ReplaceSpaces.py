def replace_spaces(s):
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate through each character in the input string
    for char in s:
        if char == ' ':
            # Replace spaces with '@40'
            result += '@40'
        else:
            # Append other characters as they are
            result += char
            
    return result

# Example usage
input_string = "Hello world, this is an example."
output_string = replace_spaces(input_string)
print(output_string)
