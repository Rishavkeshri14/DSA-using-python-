from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the elements of nums to the right by k steps.
        
        :param nums: List of integers to be rotated.
        :param k: Number of steps to rotate the list.
        """
        # Length of the list
        n = len(nums)
        
        # Create a temporary list to hold the rotated values
        temp = [0] * n
        
        # Rotate the elements using modulus to determine new positions
        for i in range(n):
            temp[(i + k) % n] = nums[i]
        
        # Copy the rotated values back to the original list
        for i in range(n):
            nums[i] = temp[i]

# Example usage:
solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution.rotate(nums, k)
print(nums)  # Output will be [5, 6, 7, 1, 2, 3, 4]
