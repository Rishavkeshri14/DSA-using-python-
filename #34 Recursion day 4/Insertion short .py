def insertion_sort(arr, idx, size):
    # Base case: If idx reaches the size of the array, sorting is complete
    if idx == size:
        return

    # Store the current element
    curr = arr[idx]
    j = idx - 1

    # Move elements of arr[0..idx-1], that are greater than curr, to one position ahead of their current position
    while j >= 0:
        if curr < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        else:
            break

    # Place the current element at its correct position
    arr[j + 1] = curr

    # Recursively sort the rest of the array
    insertion_sort(arr, idx + 1, size)

# Example usage
if __name__ == "__main__":
    # Array to be sorted
    arr = [10, 1, 7, 6, 14, 9]
    # Size of the array
    size = len(arr)

    # Start the recursive sorting
    insertion_sort(arr, 1, size)

    # Print the sorted array
    print("Sorted array:", arr)
