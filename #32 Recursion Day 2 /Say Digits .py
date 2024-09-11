# Function to recursively print the digits of a number as words
def say_digit(n, arr):
    # Base case: when n becomes 0, stop the recursion
    if n == 0:
        return

    # Get the last digit of the number
    digit = n % 10
    # Remove the last digit from the number
    n = n // 10

    # Recursive call to process the remaining digits
    say_digit(n, arr)

    # Print the word corresponding to the digit
    print(arr[digit], end=" ")

# Main code
if __name__ == "__main__":
    # List of words for digits 0 to 9
    arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    # Input number from user
    n = int(input("Enter a number: "))

    # If the number is 0, directly print "zero"
    if n == 0:
        print(arr[0])
    else:
        # Call the recursive function to print digits as words
        say_digit(n, arr)
#output
one two three
