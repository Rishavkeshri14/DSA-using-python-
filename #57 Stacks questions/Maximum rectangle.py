class Solution:
    def next_smaller_element(self, arr):
        """
        Find the next smaller element for each element in the array.
        :param arr: List[int] - the input array
        :return: List[int] - the indices of the next smaller elements
        """
        stack = []
        n = len(arr)
        ans = [-1] * n  # Initialize the answer array with -1
        
        for i in range(n - 1, -1, -1):
            curr = arr[i]
            # Maintain elements in stack such that stack[-1] < curr
            while stack and arr[stack[-1]] >= curr:
                stack.pop()
            # If stack is not empty, the next smaller element is at stack[-1]
            if stack:
                ans[i] = stack[-1]
            stack.append(i)  # Push current index onto the stack
            
        return ans

    def prev_smaller_element(self, arr):
        """
        Find the previous smaller element for each element in the array.
        :param arr: List[int] - the input array
        :return: List[int] - the indices of the previous smaller elements
        """
        stack = []
        n = len(arr)
        ans = [-1] * n  # Initialize the answer array with -1
        
        for i in range(n):
            curr = arr[i]
            # Maintain elements in stack such that stack[-1] < curr
            while stack and arr[stack[-1]] >= curr:
                stack.pop()
            # If stack is not empty, the previous smaller element is at stack[-1]
            if stack:
                ans[i] = stack[-1]
            stack.append(i)  # Push current index onto the stack
            
        return ans

    def largest_rectangle_area(self, heights):
        """
        Calculate the largest rectangle area in a histogram.
        :param heights: List[int] - the heights of the histogram bars
        :return: int - the maximum area found
        """
        n = len(heights)
        next_indices = self.next_smaller_element(heights)
        prev_indices = self.prev_smaller_element(heights)

        area = float('-inf')  # Initialize to negative infinity

        for i in range(n):
            # If there is no next smaller element, use n as width limit
            if next_indices[i] == -1:
                next_indices[i] = n
            # Calculate the width and area for the rectangle with height heights[i]
            width = next_indices[i] - prev_indices[i] - 1
            new_area = heights[i] * width
            area = max(area, new_area)  # Update the maximum area
            
        return area

    def max_area(self, M):
        """
        Compute the maximum area of a rectangle of 1s in a binary matrix.
        :param M: List[List[int]] - the binary matrix
        :return: int - the maximum area found
        """
        if not M:
            return 0  # Edge case: empty matrix
        
        n = len(M)
        m = len(M[0])
        
        # Compute area for the first row
        area = self.largest_rectangle_area(M[0])
        
        # Update each row based on previous row
        for i in range(1, n):
            for j in range(m):
                # Update the current row by adding the previous row's value
                if M[i][j] != 0:
                    M[i][j] += M[i - 1][j]
                else:
                    M[i][j] = 0
            
            # Calculate the maximum area for the updated row
            area = max(area, self.largest_rectangle_area(M[i]))
        
        return area

# Example usage
if __name__ == "__main__":
    # Number of test cases
    T = 1
    # Example binary matrix (1s and 0s)
    M = [
        [0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    
    # Initialize the Solution class
    solution = Solution()
    # Print the maximum area of a rectangle of 1s
    print("Maximum area of rectangle of 1s:", solution.max_area(M))
