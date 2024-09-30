class SpecialStack:
    def __init__(self):
        # Initialize the stack and minimum value.
        self.s = []  # This will store the elements of the stack.
        self.mini = float('inf')  # Initialize mini to positive infinity.

    def push(self, data):
        """Push an element onto the stack."""
        if not self.s:  # If the stack is empty
            self.s.append(data)
            self.mini = data  # Set the minimum to the first element
        else:
            if data < self.mini:  # If the new data is less than current minimum
                # Store modified value in stack
                self.s.append(2 * data - self.mini)
                self.mini = data  # Update the minimum
            else:
                self.s.append(data)  # Push normally

    def pop(self):
        """Pop the top element from the stack."""
        if not self.s:  # If the stack is empty
            return -1  # Return -1 for an empty stack

        curr = self.s.pop()  # Get the top element
        if curr > self.mini:  # If the current element is greater than the minimum
            return curr  # Return it normally
        else:
            # If current is equal to the minimum, retrieve the previous minimum
            prev_min = self.mini
            val = 2 * self.mini - curr  # Calculate the previous minimum
            self.mini = val  # Update the minimum
            return prev_min  # Return the previous minimum

    def top(self):
        """Get the top element of the stack."""
        if not self.s:  # If the stack is empty
            return -1

        curr = self.s[-1]  # Get the top element
        if curr < self.mini:  # If the top element is the encoded minimum
            return self.mini  # Return the current minimum
        else:
            return curr  # Return the current top

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.s) == 0

    def get_min(self):
        """Get the minimum element from the stack."""
        if self.is_empty():
            return -1  # Return -1 if the stack is empty
        return self.mini  # Return the minimum value


# Example usage:
if __name__ == "__main__":
    stack = SpecialStack()
    stack.push(10)
    stack.push(20)
    print("Current minimum:", stack.get_min())  # Output: 10
    stack.push(5)
    print("Current minimum:", stack.get_min())  # Output: 5
    print("Top element:", stack.top())           # Output: 5
    print("Popped element:", stack.pop())        # Output: 5
    print("Current minimum:", stack.get_min())   # Output: 10
    print("Top element:", stack.top())           # Output: 20
    print("Is stack empty?", stack.is_empty())   # Output: False
