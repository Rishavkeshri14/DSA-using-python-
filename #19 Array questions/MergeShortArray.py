# Function to merge two sorted arrays into a third array
def merge(arr1, arr2):
    n = len(arr1)  # Length of the first array
    m = len(arr2)  # Length of the second array
    arr3 = []  # Empty list to store merged result

    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2

    # Merging arrays based on their values
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])  # Add element from arr1 if it's smaller
            i += 1
        else:
            arr3.append(arr2[j])  # Add element from arr2 if it's smaller or equal
            j += 1

    # Add remaining elements from arr1 (if any)
    while i < n:
        arr3.append(arr1[i])
        i += 1

    # Add remaining elements from arr2 (if any)
    while j < m:
        arr3.append(arr2[j])
        j += 1

    return arr3

# Function to print the merged array
def print_array(arr):
    for elem in arr:
        print(elem, end=" ")
    print()

# Main function to execute the merge and print
if __name__ == "__main__":
    arr1 = [1, 3, 5, 7, 9]  # First sorted array
    arr2 = [2, 4, 6]        # Second sorted array

    # Merging arr1 and arr2
    merged_array = merge(arr1, arr2)

    # Printing the result
    print("Merged Array:")
    print_array(merged_array)
  
