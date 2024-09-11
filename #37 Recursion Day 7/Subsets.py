class Solution:
    def subsets(self, nums):
        # This function generates all subsets of the given list nums
        def solve(nums, output, index, ans):
            # Base case: If index is out of range of nums, add the current output to ans
            if index >= len(nums):
                ans.append(output.copy())  # Use output.copy() to avoid mutation issues
                return
            
            # Exclude the current index element and recurse
            solve(nums, output, index + 1, ans)
            
            # Include the current index element in the output
            element = nums[index]
            output.append(element)
            
            # Recurse with the updated output
            solve(nums, output, index + 1, ans)
            
            # Backtrack: remove the last element added to output to explore other subsets
            output.pop()

        # Initialize the list to store all subsets
        ans = []
        # Start the recursion with an empty output list and starting index 0
        solve(nums, [], 0, ans)
        return ans

# Example usage:
solution = Solution()
nums = [1, 2, 3]
print(solution.subsets(nums))

#output
[[],[1],[2],[3],[1,2],[2,3],[1,3],[1,2,3]]
