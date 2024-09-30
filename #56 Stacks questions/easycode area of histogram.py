# Function to compute the maximum sum based on given conditions
def max_sum(arr):
    # Initialize the result (rel) to store the maximum sum
    result = 0
    n = len(arr)
    
    # Iterate through the array
    for i in range(n):
        # Initialize the current sum for the subarray
        curr_sum = 0
        
        # Iterate to the left of the current element
        for j in range(i, -1, -1):  # Reverse direction loop from i to 0
            if arr[j] <= arr[i]:  # Check if element is less than or equal to arr[i]
                curr_sum += arr[i]
            else:
                break  # Break if the condition is not met

        # Iterate to the right of the current element
        for j in range(i + 1, n):
            if arr[j] >= arr[i]:  # Check if the element is greater than or equal to arr[i]
                curr_sum += arr[i]
            else:
                break  # Break if the condition is not met
        
        # Update the result with the maximum sum found
        result = max(result, curr_sum)
    
    # Return the maximum result found
    return result

# Example usage:
arr = [6, 5, 1, 2, 3, 4]
print("Maximum sum:", max_sum(arr))
