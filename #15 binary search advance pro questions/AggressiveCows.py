# Function to check if it's possible to place k cows in stalls such that
# the minimum distance between any two cows is at least 'mid'.
def is_possible(stalls, k, mid, n):
    cow_count = 1  # We place the first cow at the first stall
    last_pos = stalls[0]  # The position of the last placed cow

    # Traverse the stalls to place the rest of the cows
    for i in range(1, n):
        if stalls[i] - last_pos >= mid:  # Check if we can place the next cow
            cow_count += 1  # Place the cow
            last_pos = stalls[i]  # Update the position of the last placed cow
            
            if cow_count == k:  # If all cows are placed, return True
                return True
    
    # If we are unable to place all cows with at least 'mid' distance, return False
    return False

# Function to find the largest minimum distance between any two cows
def aggressive_cows(stalls, k):
    stalls.sort()  # Sort the stalls to apply binary search
    n = len(stalls)
    
    start = 0  # The smallest possible minimum distance
    end = stalls[-1] - stalls[0]  # The largest possible minimum distance
    ans = -1  # Initialize the answer
    
    # Binary search for the largest minimum distance
    while start <= end:
        mid = start + (end - start) // 2  # Midpoint of current range
        
        # Check if it is possible to place cows with at least 'mid' distance
        if is_possible(stalls, k, mid, n):
            ans = mid  # If yes, store the result
            start = mid + 1  # Try for a larger minimum distance
        else:
            end = mid - 1  # Try for a smaller minimum distance
    
    return ans

# Example usage
stalls = [1, 2, 8, 4, 9]
k = 3  # Number of cows
result = aggressive_cows(stalls, k)
print(f"The largest minimum distance is: {result}")
