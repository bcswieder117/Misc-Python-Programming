# Blaine Swieder
# LeetCode (Python): Divide a String into Groups of Size k
# June 22nd, 2025

class Solution:
    def divideString(self, s, k, fill):
        res = []
        for i in range(0, len(s), k):
            group = s[i:i + k]
            if len(group) < k:
                group += fill * (k - len(group)) 
            res.append(group)
        return res 
    

############ Examples ################################

# Create an instance of the Solution class

sol = Solution()

# Define the input values

s = "abcdefghij"
k = 3 
fill = "x" 

# Call the method and print the result

result = sol.divideString(s, k, fill) 
print(result)  # Expected Output ['abc', 'def', 'ghi', 'jxx']














































