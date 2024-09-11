# Function to get the pivot point in a rotated sorted array
def get_pivot(arr, n):
    # Initialize start and end indices
    s = 0
    e = n - 1
    # Calculate the mid index
    mid = s + (e - s) // 2

    # Iterate until start index is less than end index
    while s < e:
        # If the mid element is greater than or equal to the first element
        # it means the pivot is in the right half, so move the start pointer to mid+1
        if arr[mid] >= arr[0]:
            s = mid + 1
        else:
            # Otherwise, move the end pointer to mid
            e = mid
        # Recalculate mid
        mid = s + (e - s) // 2

    # Return the start index as the pivot point
    return s

# Function for binary search between given start and end indices
def binary_search(arr, s, e, key):
    # Initialize start and end pointers
    start = s
    end = e
    # Calculate the mid index
    mid = start + (end - start) // 2

    # Iterate while start pointer is less than or equal to end pointer
    while start <= end:
        # If the mid element matches the key, return the index
        if arr[mid] == key:
            return mid

        # If the key is greater than the mid element, search in the right half
        if key > arr[mid]:
            start = mid + 1
        else:
            # Otherwise, search in the left half
            end = mid - 1

        # Recalculate mid
        mid = start + (end - start) // 2

    # If the element is not found, return -1
    return -1

# Main function to find the position of the given key in the rotated sorted array
def find_position(arr, n, k):
    # Find the pivot index
    pivot = get_pivot(arr, n)

    # If the key is between the pivot element and the last element, search in the second half
    if k >= arr[pivot] and k <= arr[n-1]:
        return binary_search(arr, pivot, n-1, k)
    else:
        # Otherwise, search in the first half
        return binary_search(arr, 0, pivot - 1, k)


# Example usage
arr = [7, 9, 1, 2, 3]  # Rotated sorted array
n = len(arr)  # Length of the array
key = 2  # Element to search

# Find the position of the key
position = find_position(arr, n, key)

# Output the result
if position != -1:
    print(f"Element {key} found at index {position}")
else:
    print(f"Element {key} not found in the array")
