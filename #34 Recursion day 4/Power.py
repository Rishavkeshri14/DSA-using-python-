def power(a, b):
    # Base case: if exponent is 0, return 1
    if b == 0:
        return 1
    
    # Base case: if exponent is 1, return the base itself
    if b == 1:
        return a

    # Recursive call: compute power of a^(b//2)
    ans = power(a, b // 2)

    # If b is even, return ans^2
    if b % 2 == 0:
        return ans * ans
    else:
        # If b is odd, return a * ans^2
        return a * ans * ans

# Main function to take input and display output
def main():
    # Read input values for base and exponent
    a = int(input("Enter base (a): "))
    b = int(input("Enter exponent (b): "))

    # Compute the result using the power function
    result = power(a, b)

    # Display the result
    print(f"Answer is {result}")

# Call the main function
if __name__ == "__main__":
    main()
