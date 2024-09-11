# Import the required module for taking user input
import sys

# Function to calculate the factorial of a number using recursion
def factorial(n):
    # Base case: If the input is 0, the factorial is 1
    if n == 0:
        return 1
    # Recursive case: Multiply the number by the factorial of (n-1)
    return n * factorial(n - 1)

# Main function
if __name__ == "__main__":
    # Take input from the user
    try:
        n = int(input("Enter a number to find its factorial: "))
        
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        
        # Call the factorial function and store the result
        fact = factorial(n)
        
        # Print the result
        print(f"Factorial of {n} is: {fact}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")
      
