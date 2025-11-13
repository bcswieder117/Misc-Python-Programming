# Blaine Swieder
# LeetCode (Python3): Reschedule Meetings for Maximum Free Time II
# July 10th, 2025

from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        # 1) sort the meetings by start time
        meetings = sorted(zip(startTime, endTime))
        start = [s for s, _ in meetings]
        end   = [e for _, e in meetings]

        # 2) build the gaps array g of length n+1
        #    g[0] = free before the first meeting
        #    g[i] = free between meeting i-1 and i   (1 <= i <= n-1)
        #    g[n] = free after the last meeting
        g = [0] * (n + 1)
        g[0] = start[0]
        for i in range(1, n):
            g[i] = start[i] - end[i-1]
        g[n] = eventTime - end[n-1]

        # 3) compute the original maximum free span
        ans = max(g)

        # 4) prefix‐max and suffix‐max over g for O(1) exclude‐queries
        pre = [0] * (n + 1)
        pre[0] = g[0]
        for i in range(1, n + 1):
            pre[i] = max(pre[i-1], g[i])

        suf = [0] * (n + 1)
        suf[n] = g[n]
        for i in range(n-1, -1, -1):
            suf[i] = max(suf[i+1], g[i])

        # 5) try removing each meeting i
        for i in range(n):
            dur = end[i] - start[i]
            # free_i = sum of the two gaps that border meeting i
            free_i = g[i] + g[i+1]
            merged = free_i + dur  # how big the gap would be if you didn't reinsert

            # max gap excluding g[i] and g[i+1]
            left_max  = pre[i-1]     if i-1 >= 0   else 0
            right_max = suf[i+2]     if i+2 <= n   else 0
            excl_max  = max(left_max, right_max)

            # if there's some other gap that can fit duration, you get the full merged gap
            if excl_max >= dur:
                best_i = merged
            else:
                # otherwise you have to reinsert inside the merged gap at best free_i,
                # or possibly leave excl_max if it's larger
                best_i = max(free_i, excl_max)

            ans = max(ans, best_i)

        return ans


#### Example Usage ###########################################

sol = Solution()
examples = [
    (5,   [1, 3],       [2, 5],       2),
    (10,  [0, 7, 9],    [1, 8, 10],   7),
    (10,  [0, 3, 7, 9], [1, 4, 8, 10],6),
    (5,   [0, 1, 2, 3, 4],[1, 2, 3, 4, 5],0),
]

for idx, (et, st, en, exp) in enumerate(examples, 1):
    res = sol.maxFreeTime(et, st, en)
    print(f"Example {idx}: We got {res}, and we expected {exp}")
