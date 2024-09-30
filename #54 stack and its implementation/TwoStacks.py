class TwoStack:
    # Initialize TwoStack.
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size  # Array of given size to hold elements of both stacks
        self.top1 = -1            # Top pointer for Stack 1
        self.top2 = size          # Top pointer for Stack 2

    # Push in stack 1.
    def push1(self, num):
        # Ensure there is at least one empty space for the new element
        if self.top2 - self.top1 > 1:
            self.top1 += 1
            self.arr[self.top1] = num
        else:
            print("Stack Overflow for Stack 1")

    # Push in stack 2.
    def push2(self, num):
        # Ensure there is at least one empty space for the new element
        if self.top2 - self.top1 > 1:
            self.top2 -= 1
            self.arr[self.top2] = num
        else:
            print("Stack Overflow for Stack 2")

    # Pop from stack 1 and return the popped element.
    def pop1(self):
        # Check if there are elements to pop from Stack 1
        if self.top1 >= 0:
            ans = self.arr[self.top1]
            self.top1 -= 1
            return ans
        else:
            return -1  # Return -1 if Stack 1 is empty

    # Pop from stack 2 and return the popped element.
    def pop2(self):
        # Check if there are elements to pop from Stack 2
        if self.top2 < self.size:
            ans = self.arr[self.top2]
            self.top2 += 1
            return ans
        else:
            return -1  # Return -1 if Stack 2 is empty

# Example Usage:

# Initialize two stacks with a total size of 6
two_stack = TwoStack(6)

# Push elements into Stack 1
two_stack.push1(5)
two_stack.push1(10)
two_stack.push1(15)

# Push elements into Stack 2
two_stack.push2(20)
two_stack.push2(25)
two_stack.push2(30)

# Pop elements from Stack 1
print(two_stack.pop1())  # Output: 15
print(two_stack.pop1())  # Output: 10

# Pop elements from Stack 2
print(two_stack.pop2())  # Output: 30
print(two_stack.pop2())  # Output: 25
