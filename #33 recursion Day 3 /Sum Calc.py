def get_sum(arr, size):
    """
    Recursive function to calculate the sum of elements in an array.
    
    Parameters:
    arr (list): The list of integers.
    size (int): The number of elements in the list to consider.
    
    Returns:
    int: The sum of the elements.
    """
    # Base case: if the size of the array is 0, return 0
    if size == 0:
        return 0
    
    # Base case: if there is only one element, return that element
    if size == 1:
        return arr[0]
    
    # Recursive case: sum the first element with the sum of the remaining part of the array
    remaining_part = get_sum(arr[1:], size - 1)
    sum = arr[0] + remaining_part
    return sum

def main():
    # Initialize the array and size
    arr = [2, 4, 9, 9, 9]
    size = len(arr)  # Size of the array
    
    # Calculate the sum using the recursive function
    sum = get_sum(arr, size)
    
    # Print the result
    print(f"Sum is {sum}")

# Run the main function
if __name__ == "__main__":
    main()
  
