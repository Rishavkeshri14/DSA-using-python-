class Solution:
    def spiralOrder(self, matrix):
        # Resultant list to store the spiral order
        result = []

        # Get the number of rows and columns in the matrix
        if not matrix or not matrix[0]:
            return result
        
        rows = len(matrix)
        cols = len(matrix[0])

        # Total number of elements to traverse
        total_elements = rows * cols
        count = 0

        # Initialize the pointers for the four boundaries
        start_row = 0
        end_row = rows - 1
        start_col = 0
        end_col = cols - 1

        # Traverse the matrix in spiral order
        while count < total_elements:
            # Traverse from left to right across the top row
            for i in range(start_col, end_col + 1):
                if count < total_elements:
                    result.append(matrix[start_row][i])
                    count += 1
            start_row += 1  # Move the top boundary down

            # Traverse from top to bottom along the right column
            for i in range(start_row, end_row + 1):
                if count < total_elements:
                    result.append(matrix[i][end_col])
                    count += 1
            end_col -= 1  # Move the right boundary left

            # Traverse from right to left across the bottom row
            for i in range(end_col, start_col - 1, -1):
                if count < total_elements:
                    result.append(matrix[end_row][i])
                    count += 1
            end_row -= 1  # Move the bottom boundary up

            # Traverse from bottom to top along the left column
            for i in range(end_row, start_row - 1, -1):
                if count < total_elements:
                    result.append(matrix[i][start_col])
                    count += 1
            start_col += 1  # Move the left boundary right

        return result

# Example usage:
if __name__ == "__main__":
    # Define a sample matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Create an instance of the solution class
    sol = Solution()

    # Get the spiral order of the matrix
    spiral_order = sol.spiralOrder(matrix)

    # Print the result
    print(spiral_order)  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
