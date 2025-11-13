# Blaine Swieder
# Leetcode (Python3): Meetings III
# July 11th, 2025

import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 1) Sort meetings by start time
        meetings.sort(key=lambda x: x[0])
        
        # 2) Min-heap of free room indices
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        # 3) Min-heap of (end_time, room_idx) for busy rooms
        busy_rooms = []
        
        # 4) Count of meetings per room
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Release all rooms freed by 'start'
            while busy_rooms and busy_rooms[0][0] <= start:
                freed_time, r = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, r)
            
            if free_rooms:
                # Assign immediately
                room = heapq.heappop(free_rooms)
                finish = end
            else:
                # Delay until the earliest room is free
                freed_time, room = heapq.heappop(busy_rooms)
                finish = freed_time + duration
            
            # Record and mark busy
            count[room] += 1
            heapq.heappush(busy_rooms, (finish, room))
        
        # Find the room with the max meetings (break ties by lower index)
        max_meet = max(count)
        for i, c in enumerate(count):
            if c == max_meet:
                return i


####### Example Usage ############################################################

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        # Example 1
        {
            "n": 2,
            "meetings": [[0,10],[1,5],[2,7],[3,4]],
            "expected": 0
        },
        # Example 2
        {
            "n": 3,
            "meetings": [[1,20],[2,10],[3,5],[4,9],[6,8]],
            "expected": 1
        },
    ]

    for idx, tc in enumerate(test_cases, 1):
        n = tc["n"]
        meetings = tc["meetings"][:]   # copy, since our method sorts in place
        got = sol.mostBooked(n, meetings)
        print(f"Case {idx}: mostBooked(n = {n}, meetings = {tc['meetings']})")
        print(f"    We expected → {tc['expected']}, and we got → {got}\n")
