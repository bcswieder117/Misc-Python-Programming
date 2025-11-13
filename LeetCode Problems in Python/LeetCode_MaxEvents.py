# Blaine Swieder
# LeetCode (Python3): Max Number of Events that can be Attended II
# July 8th, 2025

from bisect import bisect_left
from functools import lru_cache
from typing import List          # ← add this when running outside LeetCode

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # 1. sort events by start-day (ascending); O(n log n)
        events.sort()

        # 2. collect start days for binary search look-ups
        start_days = [e[0] for e in events]

        # 3. top-down DP with memoisation
        @lru_cache(maxsize=None)
        def dp(i: int, remaining: int) -> int:
            if i == len(events) or remaining == 0:
                return 0

            # option A – skip current event
            best = dp(i + 1, remaining)

            # option B – take current event, then jump to next non-overlapping
            next_i = bisect_left(start_days, events[i][1] + 1)
            best = max(best, events[i][2] + dp(next_i, remaining - 1))
            return best

        return dp(0, k)

######## Examples ##############################################

if __name__ == "__main__":
    events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]
    k = 2
    print(Solution().maxValue(events, k))   # Desired Output: 7
