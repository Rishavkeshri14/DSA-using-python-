def merge_sort(arr, s, e):
    """
    Perform merge sort on the array `arr` from index `s` to index `e`.
    """
    # Base case: if the subarray has one or zero elements, it's already sorted
    if s >= e:
        return

    mid = (s + e) // 2
    # Recursively sort the left half
    merge_sort(arr, s, mid)
    # Recursively sort the right half
    merge_sort(arr, mid + 1, e)
    # Merge the sorted halves
    merge(arr, s, mid, e)

def merge(arr, s, mid, e):
    """
    Merge two sorted subarrays of `arr`.
    The first subarray is `arr[s:mid+1]` and the second subarray is `arr[mid+1:e+1]`.
    """
    len1 = mid - s + 1  # Length of the first subarray
    len2 = e - mid      # Length of the second subarray

    # Create temporary arrays
    arr1 = arr[s:mid+1]
    arr2 = arr[mid+1:e+1]

    # Merge the temporary arrays back into arr
    idx1 = 0  # Index for arr1
    idx2 = 0  # Index for arr2
    originalArrayIndex = s  # Index for the main array

    while idx1 < len1 and idx2 < len2:
        if arr1[idx1] < arr2[idx2]:
            arr[originalArrayIndex] = arr1[idx1]
            idx1 += 1
        else:
            arr[originalArrayIndex] = arr2[idx2]
            idx2 += 1
        originalArrayIndex += 1

    # Copy any remaining elements of arr1
    while idx1 < len1:
        arr[originalArrayIndex] = arr1[idx1]
        idx1 += 1
        originalArrayIndex += 1

    # Copy any remaining elements of arr2
    while idx2 < len2:
        arr[originalArrayIndex] = arr2[idx2]
        idx2 += 1
        originalArrayIndex += 1

def main():
    arr = [8, 9, 2, 5, 1]
    size = len(arr)

    print("Before Sorting:")
    print(arr)

    merge_sort(arr, 0, size - 1)

    print("After Sorting:")
    print(arr)

if __name__ == "__main__":
    main()
  
