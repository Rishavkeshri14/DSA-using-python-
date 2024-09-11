def quick_sort(arr, s, e):
    # Base case: if the start index is greater than or equal to the end index
    if s >= e:
        return

    # Partition the array and get the index of the pivot
    p = partition(arr, s, e)

    # Recursively sort the left part
    quick_sort(arr, s, p - 1)

    # Recursively sort the right part
    quick_sort(arr, p + 1, e)

def partition(arr, s, e):
    # Choose the pivot as the first element
    pivot = arr[s]
    count = 0

    # Count elements smaller than or equal to pivot
    for i in range(s + 1, e + 1):
        if arr[i] <= pivot:
            count += 1

    # Place the pivot element in its correct position
    pivot_idx = s + count
    arr[s], arr[pivot_idx] = arr[pivot_idx], arr[s]

    s_idx = s
    e_idx = e

    # Rearrange elements around the pivot
    while s_idx < pivot_idx and e_idx > pivot_idx:
        # Move s_idx to the right as long as elements are <= pivot
        while s_idx < pivot_idx and arr[s_idx] <= pivot:
            s_idx += 1
        # Move e_idx to the left as long as elements are > pivot
        while e_idx > pivot_idx and arr[e_idx] > pivot:
            e_idx -= 1
        # Swap elements if necessary
        if s_idx < pivot_idx and e_idx > pivot_idx:
            arr[s_idx], arr[e_idx] = arr[e_idx], arr[s_idx]
            s_idx += 1
            e_idx -= 1

    return pivot_idx

# Example usage
if __name__ == "__main__":
    arr = [6, 6, -6, -2, -4, -6, 2, -6]
    size = len(arr)

    quick_sort(arr, 0, size - 1)

    print("Sorted array:")
    for num in arr:
        print(num, end=" ")
