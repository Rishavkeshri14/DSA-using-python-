# Function to print the elements of the array along with its size
def print_array(arr):
    # Print the size of the array
    print("Size of array is", len(arr))

    # Loop to print each element in the array
    for i in arr:
        print(i, end=" ")
    print()  # For new line after printing array elements

# Recursive function for linear search
def linear_search(arr, k):
    # Print the current array and its size
    print_array(arr)

    # Base case: If the array is empty, return False
    if len(arr) == 0:
        return False

    # If the first element matches the key, return True
    if arr[0] == k:
        return True
    else:
        # Recursive case: search the rest of the array
        return linear_search(arr[1:], k)

# Main code to test the functions
if __name__ == "__main__":
    # Example array
    arr = [3, 5, 1, 2, 6]
    
    # Key to search for
    key = 6

    # Call the linear_search function
    found = linear_search(arr, key)

    # Print if the key is present or absent
    if found:
        print("Present")
    else:
        print("Absent")
#output
Size of array is 5
3 5 1 2 6 
Size of array is 4
5 1 2 6 
Size of array is 3
1 2 6 
Size of array is 2
2 6 
Size of array is 1
6 
Present
