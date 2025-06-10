from collections import Counter

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)
        odd_freqs = []
        even_freqs = []

        for count in freq.values():
            if count % 2 == 1:
                odd_freqs.append(count)
            else:
                even_freqs.append(count)

        if not odd_freqs or not even_freqs:
            return 0

        # Try all combinations of odd - even
        max_diff = float('-inf')
        for o in odd_freqs:
            for e in even_freqs:
                max_diff = max(max_diff, o - e)

        return max_diff

        
        
        
if __name__ == "__main__":
    inputs = ["aaaaabbc", "abcabcab", "aabbcc"]
    for s in inputs:
        print(f"{s} → {Solution().maxDifference(s)}")
