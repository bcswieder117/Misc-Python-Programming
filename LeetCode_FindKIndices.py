# Blaine Swieder
# LeetCode (Python): Find All k-Distant Indices in an Array
# June 23rd, 2025

class Solution:
    def findKDistantIndices(self, nums, key, k): 
        res = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) <= k and nums[j] == key:
                    res.append(i)
                    break
        return res
    

########### Examples ##################################

# Create a Solution object

sol = Solution()

# Define the Input

nums = [3, 4, 9, 1, 3, 9, 5]
key = 9
k = 1

# Call the Method

result = sol.findKDistantIndices(nums, key, k)

# Print the Result

print(result)  # Output: [1, 2, 3, 4, 5, 6]