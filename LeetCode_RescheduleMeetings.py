# Blaine Swieder
# LeetCode (Python3): Reschedule Meetings for Max Free Time I
# July 9th, 2025

from typing import List
from collections import deque

class Solution:
    def maxFreeTime(self, eventTime: int, k: int,
                    startTime: List[int], endTime: List[int]) -> int:

        n = len(startTime)
        if k == 0:                       # nothing can move → current longest gap
            prev, best = 0, 0
            for s, e in zip(startTime, endTime):
                best = max(best, s - prev)
                prev = e
            best = max(best, eventTime - prev)
            return best

        # durations and prefix-sums
        dur   = [e - s for s, e in zip(startTime, endTime)]
        pref  = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + dur[i]

        # helper array A[i] = pref[i] - (end[i-1] if i>0 else 0)
        A = [0] * n
        for i in range(n):
            left = 0 if i == 0 else endTime[i - 1]
            A[i] = pref[i] - left

        ans, dq = 0, deque()             # deque stores indices with decreasing A

        for r in range(n):
            # push current index, keep deque decreasing
            while dq and A[r] >= A[dq[-1]]:
                dq.pop()
            dq.append(r)

            # keep only indices within last k positions
            while dq and dq[0] < r - k + 1:
                dq.popleft()

            # best l is at the front of the deque
            right = eventTime if r == n - 1 else startTime[r + 1]
            gap   = right - pref[r + 1] + A[dq[0]]
            ans   = max(ans, gap)

        return ans


########## Example Usage #######################

# Create an instance of the Solution class
sol = Solution()

# Define inputs
eventTime = 20
k = 1
startTime = [1, 5, 10]
endTime = [3, 7, 12]

# Call the method
result = sol.maxFreeTime(eventTime, k, startTime, endTime)

# Print the result
print("Maximum Free Time:", result) # Output Given should be 11. 
