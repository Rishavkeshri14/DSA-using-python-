def next_smaller_element(arr):
    # Initialize a stack to keep track of elements
    stack = []
    # Initialize the result list with -1 (default for no smaller element)
    ans = [-1] * len(arr)

    # Iterate through the array from right to left
    for i in range(len(arr) - 1, -1, -1):
        curr = arr[i]  # Current element

        # Pop elements from the stack while the stack is not empty
        # and the top of the stack is greater than or equal to the current element
        while stack and stack[-1] >= curr:
            stack.pop()

        # If the stack is not empty, the top element is the next smaller element
        if stack:
            ans[i] = stack[-1]

        # Push the current element onto the stack
        stack.append(curr)

    return ans

# Example usage
if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    result = next_smaller_element(arr)
    print("Input array:", arr)
    print("Next smaller elements:", result)
