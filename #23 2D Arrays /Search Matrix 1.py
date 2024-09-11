class Solution:
    def searchMatrix(self, matrix, target):
        # Get the number of rows and columns in the matrix
        if not matrix or not matrix[0]:
            return False

        row = len(matrix)
        col = len(matrix[0])
        
        # Initialize the start and end indices for binary search
        start = 0
        end = row * col - 1
        
        # Perform binary search
        while start <= end:
            # Calculate the middle index
            mid = start + (end - start) // 2
            
            # Convert the 1D index back to 2D coordinates
            element = matrix[mid // col][mid % col]
            
            # Check if the target is found
            if element == target:
                return True
            
            # Adjust search range based on comparison
            if element < target:
                start = mid + 1
            else:
                end = mid - 1
        
        # Target not found
        return False

# Example usage:
solution = Solution()
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
target = 5

# Search for the target in the matrix
print(solution.searchMatrix(matrix, target))  # Output: True
