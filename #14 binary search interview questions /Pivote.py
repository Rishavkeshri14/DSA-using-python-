# Function to find the pivot in a rotated sorted array
def get_pivot(arr, n):
    start = 0  # Start index
    end = n - 1  # End index
 
    # Continue searching until start is less than end
    while start <= end:
        mid = start + end) // 2  # Calculate the mid index
        # If middle element is greater than or equal to the first element,
        # then pivot must be in the right half
        if arr[mid] >= arr[0]:
            start = mid + 1
        else:
            # Otherwise, pivot is in the left half
            end = mid
        
        # Recalculate the mid index after adjusting start or end
        
    
    # Return the start index which will be the pivot index
    return start

# Example usage
if __name__ == "__main__":
    arr = [4,5,6,1,2,3]
    n = len(arr)
    print(f"Pivot is at index: {get_pivot(arr, n)}")
  
#output
Pivot is at index: 3