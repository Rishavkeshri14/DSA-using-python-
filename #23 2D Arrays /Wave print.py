# Function to perform wave print of a 2D array
def wavePrint(arr, nRows, mCols):
    # Resultant list to store the wave print elements
    ans = []
    
    # Loop through each column
    for col in range(mCols):
        # If the column index is odd, traverse from bottom to top
        if col % 2 == 1:
            for row in range(nRows - 1, -1, -1):
                ans.append(arr[row][col])
        else:
            # If the column index is even, traverse from top to bottom
            for row in range(nRows):
                ans.append(arr[row][col])
    
    return ans

# Example usage
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

nRows = len(arr)       # Number of rows in the array
mCols = len(arr[0])    # Number of columns in the array

# Call the wavePrint function
result = wavePrint(arr, nRows, mCols)

# Print the result
print("Wave Print:", result)
