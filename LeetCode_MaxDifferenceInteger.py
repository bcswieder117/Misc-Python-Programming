# Blaine Swieder
# Python Programming: Max Difference You Can Get From Changing an Integer
# Date: June 15th, 2025

class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        s = str(num)
        
        # Max Number: Replace first digit that is not 9 with 9.
        
        for ch in s:
            if ch != '9':
                max_num = int(s.replace(ch, '9'))
                break
        else: 
            max_num = num    # All digits are 9.
            
        # Min Number:
        # If first digit is not 1 -> replace it with 1.
        # Else, replace the first non-1 digit (but not at the first place) with 0.
        
        if s[0] != '1': 
            min_num = int(s.replace(s[0], '1'))
        else: 
            for ch in s[1:]:
                if ch != '0':
                    min_num = int(s.replace(ch, '0'))
                    break
            else: 
                min_num = num # Already minimal
        
        return max_num - min_num
    
# Example
sol = Solution()
num = 555
result = sol.maxDiff(num)
print("Max difference after digit replacement:", result)