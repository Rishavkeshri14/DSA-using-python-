# Function to insert an element at the bottom of the stack
def insert_at_bottom(stack, element):
    # Base case: If the stack is empty, push the element
    if not stack:
        stack.append(element)
        return

    # Remove the top element and hold it in a temporary variable
    temp = stack.pop()

    # Recursive call to insert the element at the bottom
    insert_at_bottom(stack, element)

    # Push the held element back to the stack
    stack.append(temp)

# Function to reverse the stack
def reverse_stack(stack):
    # Base case: If the stack is empty, return
    if not stack:
        return

    # Remove the top element and hold it in a temporary variable
    temp = stack.pop()

    # Recursive call to reverse the remaining stack
    reverse_stack(stack)

    # Insert the held element at the bottom of the reversed stack
    insert_at_bottom(stack, temp)

# Example usage
stack = [1, 2, 3, 4, 5]  # Initial stack
print("Original Stack:", stack)

# Call the reverse_stack function
reverse_stack(stack)
print("Reversed Stack:", stack)
