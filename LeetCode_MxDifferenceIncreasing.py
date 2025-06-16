# Blaine Swieder
# LeetCode: Maximum Difference Between Increasing Elements
# June 16th, 2025

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        min_val = nums[0]
        max_diff = -1 
        
        for i in range(1, len(nums)):
            if nums[i] > min_val: 
                max_diff = max(max_diff, nums[i] - min_val)
            else: 
                min_val = nums[i]
        
        return max_diff
    
##### Example #############################

# Let us create an instance of the Solution Class

sol = Solution()

# Call the method with the test case input. 

result = sol.maximumDifference([7, 1, 5, 4])

# Print our result

print(result) # Output should be 4.