import sys

def is_present(arr, target):
    """
    Function to check if target is present in the 2D array.
    :param arr: 2D list
    :param target: integer to search for
    :return: True if target is found, False otherwise
    """
    for row in arr:
        if target in row:
            return True
    return False

def print_col_sum(arr):
    """
    Function to print the sum of each column in the 2D array.
    :param arr: 2D list
    """
    print("Printing Column Sums ->")
    num_cols = len(arr[0])
    for col in range(num_cols):
        col_sum = sum(arr[row][col] for row in range(len(arr)))
        print(col_sum, end=" ")
    print()

def print_row_sum(arr):
    """
    Function to print the sum of each row in the 2D array.
    :param arr: 2D list
    """
    print("Printing Row Sums ->")
    for row in arr:
        row_sum = sum(row)
        print(row_sum, end=" ")
    print()

def largest_row_sum(arr):
    """
    Function to find the row with the maximum sum.
    :param arr: 2D list
    :return: Index of the row with the maximum sum
    """
    max_sum = -sys.maxsize
    row_index = -1

    for i, row in enumerate(arr):
        row_sum = sum(row)
        if row_sum > max_sum:
            max_sum = row_sum
            row_index = i

    print("The maximum sum is", max_sum)
    return row_index

def main():
    # Create a 2D array
    arr = []

    # Taking input from the user
    print("Enter the elements row by row (3 rows and 3 columns):")
    for _ in range(3):
        row = list(map(int, input().split()))
        arr.append(row)

    # Print the 2D array
    print("Printing the array:")
    for row in arr:
        print(" ".join(map(str, row)))
    
    # Uncomment the following lines to test the functions
    # target = int(input("Enter the element to search: "))
    # if is_present(arr, target):
    #     print("Element found")
    # else:
    #     print("Not Found")

    # Print column sums
    print_col_sum(arr)

    # Print row sums
    print_row_sum(arr)

    # Find and print the index of the row with the largest sum
    row_index = largest_row_sum(arr)
    print("Max row is at index", row_index)

if __name__ == "__main__":
    main()
  
