class Solution:
    def searchMatrix(self, matrix, target):
        # Get the number of rows and columns in the matrix
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Start from the top-right corner of the matrix
        row_index = 0
        col_index = cols - 1
        
        # Traverse the matrix until the target is found or the search space is exhausted
        while row_index < rows and col_index >= 0:
            element = matrix[row_index][col_index]
            
            # If the element is equal to the target, return True (found)
            if element == target:
                return True
            
            # If the element is less than the target, move down to the next row
            elif element < target:
                row_index += 1
            
            # If the element is greater than the target, move left to the previous column
            else:
                col_index -= 1
        
        # If the target is not found, return False
        return False

# Example usage:
matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

target = 5

# Create an instance of the Solution class
solution = Solution()

# Search for the target in the matrix
result = solution.searchMatrix(matrix, target)

print(f"Target {target} found: {result}")
