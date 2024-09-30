def solve(stack, x):
    # Base case: If the stack is empty, push the element 'x' and return
    if not stack:
        stack.append(x)
        return
    
    # Store the top element and pop it from the stack
    num = stack.pop()
    
    # Recursive call to insert 'x' at the bottom of the stack
    solve(stack, x)
    
    # Push the previously popped element back to the stack
    stack.append(num)

def pushAtBottom(myStack, x):
    # Call the solve function to push 'x' at the bottom
    solve(myStack, x)
    return myStack

# Example usage:
if __name__ == "__main__":
    stack = [1, 2, 3, 4]  # Stack represented as a list
    x = 0  # Element to push at the bottom
    print("Original Stack:", stack)
    pushAtBottom(stack, x)
    print("Stack after pushing at the bottom:", stack)
