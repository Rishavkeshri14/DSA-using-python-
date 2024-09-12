# Importing List from typing module to specify the list type
from typing import List

class Solution:
    
    # Function to find the pivot/peak element in the mountain array
    def find_pivot(self, v: List[int]) -> int:
        s = 0  # Start index of the array
        e = len(v) - 1  # End index of the array
        # Binary search approach
        while s < e:  # Continue until start is less than end
            mid = (s + e) // 2  # Initial midpoint 
        
            if v[mid] < v[mid + 1]:  # If middle element is less than the next element
                s = mid + 1  # Move the start to mid + 1
            else:
                e = mid  # Otherwise, move the end to mid
       
        return s  # Return the peak element index

    # Function to return the index of the peak element in a mountain array
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.find_pivot(arr)  # Call the helper function


# Example usage
arr = [1, 3, 5, 6, 4, 2]  # Mountain array example
sol = Solution()  # Create an instance of the Solution class
peak_index = sol.peakIndexInMountainArray(arr)  # Find the peak index
print(f"The peak element is at index: {peak_index}")

      
