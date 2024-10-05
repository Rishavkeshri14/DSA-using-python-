from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0  # Initialize a counter to track the number of decreasing points
        
        # Loop through the list to count decreases
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                cnt += 1
        
        # Check the transition from the last element to the first element
        if nums[-1] > nums[0]:
            cnt += 1
        
        # If there is at most one decrease, the list can be rotated to be sorted
        return cnt <= 1


# Example usage
nums1 = [3, 4, 5, 1, 2]  # Rotated version of [1, 2, 3, 4, 5], should return True
nums2 = [2, 1, 3, 4]     # Not a rotated version of a sorted array, should return False
nums3 = [1, 2, 3]        # Already sorted, should return True
nums4 = [1, 3, 2]        # One drop, should return True

solution = Solution()

print(solution.check(nums1))  # Output: True
print(solution.check(nums2))  # Output: False
print(solution.check(nums3))  # Output: True
print(solution.check(nums4))  # Output: False
