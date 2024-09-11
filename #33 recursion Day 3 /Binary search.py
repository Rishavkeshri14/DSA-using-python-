# Function to print elements of an array between given indices
def print_array(arr, s, e):
    for i in range(s, e+1):
        print(arr[i], end=" ")
    print()  # For new line after printing the array

# Function to perform binary search
def binary_search(arr, s, e, k):
    # Base case: if start index exceeds end index, element not found
    if s > e:
        return False

    # Calculate middle index
    mid = s + (e - s) // 2

    # If the element at mid is the target element, return True
    if arr[mid] == k:
        return True

    # If the target element is greater than the element at mid, search in the right half
    if arr[mid] < k:
        return binary_search(arr, mid + 1, e, k)
    # If the target element is smaller, search in the left half
    else:
        return binary_search(arr, s, mid - 1, k)

# Main function to execute the binary search
if __name__ == "__main__":
    # Initialize the array and key to search
    arr = [2, 4, 6, 10, 14, 18, 22, 38, 49, 55, 222]
    size = len(arr)
    key = 222

    # Check if the key is present in the array using binary search
    is_present = binary_search(arr, 0, size - 1, key)

    # Print the result
    print(f"Is the key {key} present? {'Yes' if is_present else 'No'}")

    # Print the array between certain indices (Example: 0 to 5)
    print_array(arr, 0, 5)
