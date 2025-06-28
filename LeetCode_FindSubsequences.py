# Blaine Swieder
# LeetCode(Python): Find Subsequences of length k with the Largest Sum
# June 28th, 2025

class Solution:
    def maxSubsequence(self, nums, k):
        
        # Step 1: Pair each number with its index
        indexed_nums = list(enumerate(nums))
        
        # Step 2: Sort by value in descending order and pick top k
        top_k = sorted(indexed_nums, key = lambda x: x[1], reverse = True)[:k]
        
        # Step 3: Sort the selected top k by their original index to keep order
        top_k_sorted = sorted(top_k, key = lambda x: x[0])
        
        #Step 4: Return just the values
        return [val in idx, val in top_k_sorted]
    

###### Example Usage #############################
 
 # Create an instance of the Solution class

sol = Solution()
 
 # Example Input

nums = [2, 1, 3, 3]
k = 2

# Call the method
result = sol.maxSubsequence(nums, k)

# Print the result
print(result)

##################################################
       