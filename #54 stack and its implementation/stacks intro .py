class Stack:
    # Constructor to initialize the stack properties
    def __init__(self, size):
        # Initialize the size of the stack
        self.size = size
        # Create an empty list to represent the stack
        self.arr = [None] * size
        # Initialize the top of the stack to -1, indicating an empty stack
        self.top = -1

    # Push method to add an element to the stack
    def push(self, element):
        if self.size - self.top > 1:
            # Increment the top and add the element to the stack
            self.top += 1
            self.arr[self.top] = element
        else:
            # Stack overflow when there's no space left
            print("Stack Overflow")

    # Pop method to remove the top element from the stack
    def pop(self):
        if self.top >= 0:
            # Decrement the top to remove the element
            self.top -= 1
        else:
            # Stack underflow when there are no elements left
            print("Stack Underflow")

    # Peek method to get the top element of the stack
    def peek(self):
        if self.top >= 0:
            # Return the top element
            return self.arr[self.top]
        else:
            # Indicate the stack is empty
            print("Stack is Empty")
            return -1

    # Method to check if the stack is empty
    def is_empty(self):
        return self.top == -1


# Example usage
if __name__ == "__main__":
    # Create a stack of size 5
    st = Stack(5)

    # Push elements onto the stack
    st.push(22)
    st.push(43)
    st.push(44)
    st.push(22)
    st.push(43)
    st.push(44)  # This will cause "Stack Overflow"

    # Peek at the top element
    print(st.peek())  # Output: 43

    # Pop elements from the stack
    st.pop()
    print(st.peek())  # Output: 22

    st.pop()
    print(st.peek())  # Output: 44

    st.pop()
    print(st.peek())  # Output: 43

    # Check if the stack is empty
    if st.is_empty():
        print("Stack is Empty mere dost")
    else:
        print("Stack is not Empty mere dost")
    
    '''
    # Python's built-in stack using list
    s = []

    # Push operation
    s.append(2)
    s.append(3)

    # Pop operation
    s.pop()

    # Printing the top element
    print(f"Top element: {s[-1]}")

    # Check if the stack is empty
    if not s:
        print("Stack is empty")
    else:
        print("Stack is not empty")

    # Size of the stack
    print(f"Size of stack: {len(s)}")
    '''
  
