def first_occ(arr, n, key):
    s, e = 0, n - 1
    ans = -1
    while s <= e:
        mid = s + (e - s) // 2
        if arr[mid] == key:
            ans = mid
            e = mid - 1  # Move left to find the first occurrence
        elif key > arr[mid]:
            s = mid + 1  # Move right
        else:
            e = mid - 1  # Move left
    return ans

def last_occ(arr, n, key):
    s, e = 0, n - 1
    ans = -1
    while s <= e:
        mid = s + (e - s) // 2
        if arr[mid] == key:
            ans = mid
            s = mid + 1  # Move right to find the last occurrence
        elif key > arr[mid]:
            s = mid + 1  # Move right
        else:
            e = mid - 1  # Move left
    return ans

def first_and_last_position(arr, n, k):
    first = first_occ(arr, n, k)
    last = last_occ(arr, n, k)
    return (first, last)
