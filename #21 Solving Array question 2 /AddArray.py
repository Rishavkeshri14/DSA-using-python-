# Function to reverse a list
def reverse(v):
    # Initialize start and end pointers
    s = 0
    e = len(v) - 1
    
    # Swap elements from start to end until the pointers meet
    while s < e:
        v[s], v[e] = v[e], v[s]
        s += 1
        e -= 1
    
    return v

# Function to find the sum of two arrays as if they represent numbers
def find_array_sum(a, n, b, m):
    # Initialize pointers for both arrays and variables for the result and carry
    i = n - 1
    j = m - 1
    ans = []
    carry = 0
    
    # Sum corresponding elements of both arrays
    while i >= 0 and j >= 0:
        val1 = a[i]
        val2 = b[j]
        
        # Calculate sum of the two digits and the carry
        sum_val = val1 + val2 + carry
        
        # Update carry and sum
        carry = sum_val // 10
        sum_val = sum_val % 10
        
        # Append the result digit to ans
        ans.append(sum_val)
        i -= 1
        j -= 1
    
    # If array 'a' is longer, add remaining digits
    while i >= 0:
        sum_val = a[i] + carry
        carry = sum_val // 10
        sum_val = sum_val % 10
        ans.append(sum_val)
        i -= 1
    
    # If array 'b' is longer, add remaining digits
    while j >= 0:
        sum_val = b[j] + carry
        carry = sum_val // 10
        sum_val = sum_val % 10
        ans.append(sum_val)
        j -= 1
    
    # If there's still a carry left, add it as a new digit
    while carry != 0:
        sum_val = carry
        carry = sum_val // 10
        sum_val = sum_val % 10
        ans.append(sum_val)
    
    # Reverse the result to get the final answer
    return reverse(ans)

# Example usage:
a = [9, 9, 9]
b = [1]

n = len(a)
m = len(b)

# Find the sum of arrays a and b
result = find_array_sum(a, n, b, m)

# Output the result
print("Sum of arrays:", result)
