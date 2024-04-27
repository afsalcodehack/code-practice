# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycleFloyds(self, head: Optional[ListNode]) -> bool:

        if head is None or head.next is None or head.next.next is None:
            return False
        slow = head
        fast = head.next

        while fast:
            if fast == slow:
                return True

            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next

        return False


    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        while curr:
            if curr.val is True:
                return True
            curr.val = True
            curr = curr.next

        return False


head = ListNode(1)
head.next = head


driver = Solution()
print(driver.hasCycleFloyds(head))
