class Solution:
    def nextSmallerElement(self, arr):
        # Create a stack to store indices and initialize with -1 for base case
        stack = [-1]
        n = len(arr)
        ans = [0] * n  # Initialize the result array

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            curr = arr[i]
            # While stack is not empty and the current element is less than or equal to
            # the element corresponding to the index at the top of the stack
            while stack[-1] != -1 and arr[stack[-1]] >= curr:
                stack.pop()  # Pop elements from the stack
            # The answer for the current index is the index at the top of the stack
            ans[i] = stack[-1]
            stack.append(i)  # Push the current index onto the stack

        return ans

    def prevSmallerElement(self, arr):
        # Create a stack to store indices and initialize with -1 for base case
        stack = [-1]
        n = len(arr)
        ans = [0] * n  # Initialize the result array

        # Traverse the array from left to right
        for i in range(n):
            curr = arr[i]
            # While stack is not empty and the current element is less than or equal to
            # the element corresponding to the index at the top of the stack
            while stack[-1] != -1 and arr[stack[-1]] >= curr:
                stack.pop()  # Pop elements from the stack
            # The answer for the current index is the index at the top of the stack
            ans[i] = stack[-1]
            stack.append(i)  # Push the current index onto the stack

        return ans

    def largestRectangleArea(self, heights):
        n = len(heights)

        # Get the indices of the next smaller element for each element
        next_smaller = self.nextSmallerElement(heights)
        # Get the indices of the previous smaller element for each element
        prev_smaller = self.prevSmallerElement(heights)

        max_area = float('-inf')  # Initialize max area to negative infinity

        # Calculate the area for each bar
        for i in range(n):
            l = heights[i]  # Height of the current bar

            # If there's no next smaller element, use n as the right boundary
            if next_smaller[i] == -1:
                next_smaller[i] = n

            # Calculate the width: next - previous - 1
            b = next_smaller[i] - prev_smaller[i] - 1
            # Calculate the new area
            new_area = l * b
            # Update the maximum area found
            max_area = max(max_area, new_area)

        return max_area

# Example usage
if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    solution = Solution()
    result = solution.largestRectangleArea(heights)
    print("The largest rectangle area is:", result)  # Output: 10
  
