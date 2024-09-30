def is_valid_parenthesis(expression):
    # Create a stack to keep track of opening brackets
    stack = []
    
    # Iterate through each character in the expression
    for ch in expression:
        # If the character is an opening bracket, push it onto the stack
        if ch in '({[':
            stack.append(ch)
        else:
            # For closing brackets, check the stack
            if stack:
                # Get the top element of the stack
                top = stack[-1]
                # Check for matching brackets
                if (ch == ')' and top == '(') or \
                   (ch == '}' and top == '{') or \
                   (ch == ']' and top == '['):
                    # If they match, pop the top element
                    stack.pop()
                else:
                    # If they don't match, return False
                    return False
            else:
                # If the stack is empty, there's no opening bracket for the closing one
                return False
    
    # If the stack is empty, all brackets matched; return True
    return len(stack) == 0

# Example usage:
expression = "{[()()]}"
if is_valid_parenthesis(expression):
    print(f"The expression '{expression}' is valid.")
else:
    print(f"The expression '{expression}' is invalid.")
