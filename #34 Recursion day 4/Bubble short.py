def bubble_sort_recursive(arr, n):
    # Base case: if the size of the array is 0 or 1, it's already sorted
    if n <= 1:
        return

    # Perform one pass of bubble sort
    for i in range(n - 1):
        # Swap if the current element is greater than the next element
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursively call bubble_sort_recursive with a reduced array size
    bubble_sort_recursive(arr, n - 1)

def main():
    # Array to be sorted
    arr = [2, 8, 4, 9, 5]
    
    # Size of array
    n = len(arr)
    
    # Printing array before sorting
    print("Before sorting:")
    print(arr)
    
    # Call the recursive bubble sort function
    bubble_sort_recursive(arr, n)
    
    # Print array after sorting
    print("After sorting:")
    print(arr)

# Entry point of the program
if __name__ == "__main__":
    main()
