# Function to find the pivot in a rotated sorted array
def get_pivot(arr, n):
    start = 0  # Start index
    end = n - 1  # End index
    mid = start + (end - start) // 2  # Calculate the mid index
    
    # Continue searching until start is less than end
    while start < end:
        # If middle element is greater than or equal to the first element,
        # then pivot must be in the right half
        if arr[mid] >= arr[0]:
            start = mid + 1
        else:
            # Otherwise, pivot is in the left half
            end = mid
        
        # Recalculate the mid index after adjusting start or end
        mid = start + (end - start) // 2
    
    # Return the start index which will be the pivot index
    return start

# Example usage
if __name__ == "__main__":
    arr = [1, 3, 8, 10, 17]
    n = len(arr)
    print(f"Pivot is at index: {get_pivot(arr, n)}")
  
