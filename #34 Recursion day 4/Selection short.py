def selection_sort(arr):
    """
    Sorts an array in place using the Selection Sort algorithm.
    :param arr: List of elements to be sorted.
    """
    size = len(arr)  # Get the size of the array

    def sort(idx):
        # Base case: If the index is at the end of the array, return
        if idx == size:
            return

        smallest_idx = idx  # Assume the current index element is the smallest

        # Find the smallest element in the remaining unsorted part of the array
        for i in range(idx + 1, size):
            if arr[smallest_idx] > arr[i]:
                smallest_idx = i  # Update the index of the smallest element found

        # Swap the smallest element found with the element at the current index
        arr[idx], arr[smallest_idx] = arr[smallest_idx], arr[idx]

        # Recursively sort the rest of the array
        sort(idx + 1)

    sort(0)  # Start the sorting process from index 0

# Example usage
arr = [6, 2, 8, 4, 10]
selection_sort(arr)
print(arr)  # Output the sorted array
