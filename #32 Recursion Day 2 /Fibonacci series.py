# Define a class Fibonacci
class Fibonacci:
    # Define a method to calculate Fibonacci of a number 'n'
    def fib(self, n):
        # Base case: if 'n' is 0 or 1, return 'n' itself
        if n <= 1:
            return n
        # Recursive case: sum of previous two Fibonacci numbers
        return self.fib(n - 1) + self.fib(n - 2)

# Example usage
fib_obj = Fibonacci()  # Create an object of the Fibonacci class
n = 10  # Define the nth Fibonacci number to calculate
result = fib_obj.fib(n)  # Call the fib method
print(f"The {n}th Fibonacci number is: {result}")
