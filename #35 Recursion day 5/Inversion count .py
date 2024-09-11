def inversion_count(arr):
    """
    Function to count inversions in the array.
    :param arr: Input array
    :return: Total number of inversions
    """
    def count(arr, s, e):
        # Base case: single element or invalid range
        if s >= e:
            return 0

        # Find the middle point
        mid = (s + e) // 2

        # Count inversions in the left half, right half, and during merging
        inv = count(arr, s, mid)
        inv += count(arr, mid + 1, e)
        inv += merge(arr, s, e)
        return inv

    def merge(arr, s, e):
        """
        Merge two halves and count inversions.
        :param arr: Array to be sorted
        :param s: Start index of the left subarray
        :param e: End index of the right subarray
        :return: Number of inversions found
        """
        ans = 0
        mid = (s + e) // 2

        # Calculate lengths of the two subarrays
        l1 = mid - s + 1
        l2 = e - mid

        # Create temporary arrays for left and right subarrays
        a1 = arr[s:mid + 1]
        a2 = arr[mid + 1:e + 1]

        idx1 = 0
        idx2 = 0
        idx = s

        # Merge the two subarrays while counting inversions
        while idx1 < l1 and idx2 < l2:
            if a1[idx1] > a2[idx2]:
                ans += (l1 - idx1)
                arr[idx] = a2[idx2]
                idx2 += 1
            else:
                arr[idx] = a1[idx1]
                idx1 += 1
            idx += 1

        # Copy remaining elements of a1, if any
        while idx1 < l1:
            arr[idx] = a1[idx1]
            idx1 += 1
            idx += 1

        # Copy remaining elements of a2, if any
        while idx2 < l2:
            arr[idx] = a2[idx2]
            idx2 += 1
            idx += 1

        return ans

    return count(arr, 0, len(arr) - 1)


# Example usage:
arr = [2, 3, 8, 6, 1]
print(f"Number of inversions are {inversion_count(arr)}")

