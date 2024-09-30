def solve(input_stack, count, size):
    # Base case: If count reaches the middle index, pop the middle element
    if count == size // 2:
        input_stack.pop()  # Removing the middle element
        return

    # Store the top element of the stack and pop it
    num = input_stack.pop()

    # Recursive call to reach the middle element
    solve(input_stack, count + 1, size)

    # After removing the middle element, push the elements back to the stack
    input_stack.append(num)


def delete_middle(input_stack, N):
    count = 0
    # Call the recursive function to delete the middle element
    solve(input_stack, count, N)


# Example usage
if __name__ == "__main__":
    input_stack = [1, 2, 3, 4, 5]  # Example stack
    N = len(input_stack)  # Size of the stack

    print("Original stack:", input_stack)
    delete_middle(input_stack, N)
    print("Stack after deleting middle element:", input_stack)
