# Importing the necessary module
from collections import deque

# Function to find redundant brackets
def find_redundant_brackets(expression):
    # Using deque to implement stack
    stack = deque()

    # Loop through each character in the expression
    for ch in expression:
        # If the character is an opening bracket or an operator, push it to the stack
        if ch == '(' or ch in '+-*/':
            stack.append(ch)
        else:
            # If the character is a closing bracket
            if ch == ')':
                is_redundant = True

                # Pop the stack until an opening bracket '(' is found
                while stack and stack[-1] != '(':
                    top = stack.pop()
                    # If there is an operator, it's not redundant
                    if top in '+-*/':
                        is_redundant = False
                
                # Pop the opening bracket '('
                stack.pop()

                # If redundant, return True
                if is_redundant:
                    return True

    # If no redundant brackets are found, return False
    return False

# Example usage
expression = "((a+b))"  # This has redundant brackets
result = find_redundant_brackets(expression)

if result:
    print(f"The expression '{expression}' has redundant brackets.")
else:
    print(f"The expression '{expression}' does not have redundant brackets.")
  
