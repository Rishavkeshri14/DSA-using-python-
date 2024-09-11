# Function to find the integer part of the square root using binary search
def sqrt_integer(n):
    start = 0
    end = n
    mid = start + (end - start) // 2  # Calculate the middle point
    
    ans = -1  # Initialize answer to -1 (in case the exact square root is not found)
    
    # Binary search loop to find the integer part of the square root
    while start <= end:
        square = mid * mid  # Calculate the square of mid
        
        if square == n:  # If the square equals n, return mid (exact square root found)
            return mid
        elif square < n:  # If square is less than n, update start to search the upper half
            ans = mid  # Update ans to the latest mid value
            start = mid + 1
        else:  # If square is greater than n, search the lower half
            end = mid - 1
        
        mid = start + (end - start) // 2  # Recalculate mid
    
    return ans  # Return the integer part of the square root

# Function to refine the square root result to the specified precision
def more_precision(n, precision, temp_sol):
    factor = 1.0
    ans = temp_sol  # Start with the integer part of the square root

    # Loop through the required precision
    for i in range(precision):
        factor /= 10  # Decrease factor by 10 times each iteration

        # Refine the answer using small increments (factor)
        while (ans + factor) * (ans + factor) <= n:
            ans += factor  # Update answer by adding factor
    
    return ans

# Main function
if __name__ == "__main__":
    # Input the number from the user
    n = int(input("Enter the number: "))

    # Step 1: Find the integer part of the square root
    temp_sol = sqrt_integer(n)

    # Step 2: Refine the result to the desired precision (e.g., 3 decimal places)
    result = more_precision(n, 3, temp_sol)

    # Output the final result
    print(f"The square root of {n} is approximately {result}")
