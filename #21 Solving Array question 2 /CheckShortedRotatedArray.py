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
