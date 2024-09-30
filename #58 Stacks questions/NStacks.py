class NStack:
    def __init__(self, N, S):
        """
        Initialize the NStack data structure.

        :param N: Number of stacks
        :param S: Size of the array to hold stack elements
        """
        self.n = N  # Number of stacks
        self.s = S  # Size of the array
        self.arr = [0] * self.s  # Array to hold stack elements
        self.top = [-1] * self.n  # Array to track the top index of each stack
        self.next = [i + 1 for i in range(self.s)]  # Array to track the next free index
        self.next[self.s - 1] = -1  # End of the free spots linked list
        self.freespot = 0  # Pointer to the first free index

    def push(self, x, m):
        """
        Push an element 'x' onto the Mth stack.

        :param x: The element to be pushed
        :param m: The index of the stack (1-based)
        :return: True if pushed successfully, False if overflow occurs
        """
        # Check for overflow
        if self.freespot == -1:
            return False

        # Find index for the new element
        index = self.freespot

        # Insert element into array
        self.arr[index] = x

        # Update freespot to point to the next free index
        self.freespot = self.next[index]

        # Update next to point to the current top of stack m
        self.next[index] = self.top[m - 1]

        # Update the top of stack m to the new index
        self.top[m - 1] = index

        return True

    def pop(self, m):
        """
        Pop the top element from the Mth stack.

        :param m: The index of the stack (1-based)
        :return: The popped element if successful, -1 if the stack is empty
        """
        # Check underflow condition
        if self.top[m - 1] == -1:
            return -1

        # Get the index of the top element
        index = self.top[m - 1]

        # Update the top of the stack to the next element
        self.top[m - 1] = self.next[index]

        # Free up the index and point it to the current freespot
        self.next[index] = self.freespot

        # Update freespot to the index we just popped
        self.freespot = index

        return self.arr[index]


# Example usage
if __name__ == "__main__":
    # Create 3 stacks with a total size of 10
    n_stacks = NStack(3, 10)

    # Push elements onto the stacks
    print(n_stacks.push(10, 1))  # True
    print(n_stacks.push(20, 2))  # True
    print(n_stacks.push(30, 1))  # True
    print(n_stacks.push(40, 3))  # True

    # Pop elements from the stacks
    print(n_stacks.pop(1))  # 30
    print(n_stacks.pop(2))  # 20
    print(n_stacks.pop(3))  # 40
    print(n_stacks.pop(1))  # 10
    print(n_stacks.pop(1))  # -1 (stack is empty)
