# Function to check if it is possible to allocate books such that no student 
# gets more than `mid` pages
def is_possible(arr, n, m, mid):
    student_count = 1
    page_sum = 0
    
    # Iterate through each book
    for i in range(n):
        # If adding this book's pages doesn't exceed `mid`, add it to the current student's allocation
        if page_sum + arr[i] <= mid:
            page_sum += arr[i]
        else:
            # Allocate books to a new student
            student_count += 1
            if student_count > m or arr[i] > mid:
                return False
            # Start the next student's allocation with the current book
            page_sum = arr[i]
            
        # If number of students exceeds `m`, return False
        if student_count > m:
            return False
            
    return True

# Function to allocate books to minimize the maximum pages assigned to a student
def allocate_books(arr, n, m):
    # If number of students is greater than the number of books, allocation is impossible
    if m > n:
        return -1
    
    # Start with 0 pages and the sum of all pages as the initial bounds
    start = 0
    total_pages = sum(arr)
    end = total_pages
    result = -1
    
    # Binary search to find the optimal solution
    while start <= end:
        mid = start + (end - start) // 2
        
        # Check if it is possible to allocate with `mid` as the upper limit of pages per student
        if is_possible(arr, n, m, mid):
            result = mid  # Found a possible solution, try to minimize further
            end = mid - 1
        else:
            start = mid + 1
            
    return result

# Example usage
books = [12, 34, 67, 90]  # Array representing the number of pages in each book
n = len(books)  # Number of books
students = 2  # Number of students

# Call the function to find the minimum possible maximum pages allocation
result = allocate_books(books, n, students)
print(f"The minimum possible maximum pages each student can be assigned is: {result}")
