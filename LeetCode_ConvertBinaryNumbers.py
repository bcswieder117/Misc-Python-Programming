# Blaine Swieder
# LeetCode(Python3): Convert Binary Number in a Linked List to Integer
# July 14th, 2025

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = 0
        node = head
        while node:
            # shift accumulated bits left by 1, add current bit
            num = (num << 1) | node.val
            node = node.next
        return num

### Example Usage ################################################

# Example 1
n1 = ListNode(1)
n2 = ListNode(0)
n3 = ListNode(1)
n1.next = n2
n2.next = n3

print(Solution().getDecimalValue(n1))  # Expected Output: 5

# Example 2
single = ListNode(0)
print(Solution().getDecimalValue(single))  # Expected Output: 0
