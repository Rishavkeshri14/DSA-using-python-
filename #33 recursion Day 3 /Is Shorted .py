def is_sorted(arr):
    """
    Recursive function to check if an array is sorted in non-decreasing order.
    
    Parameters:
    arr (list): List of integers to check
    
    Returns:
    bool: True if the list is sorted, False otherwise
    """
    # Base case: if the array is empty or has only one element, it is sorted
    if len(arr) == 0 or len(arr) == 1:
        return True

    # Check if the first element is greater than the second element
    if arr[0] > arr[1]:
        return False
    else:
        # Recursively check the rest of the array
        return is_sorted(arr[1:])

# Example usage
arr = [2, 4, 9, 9, 9]
if is_sorted(arr):
    print("Array is sorted")
else:
    print("Array is not sorted")
  
