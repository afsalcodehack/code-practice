# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        lastNode = head

        while lastNode.next is not None:
            lastNode = lastNode.next

        print(head.val, lastNode.val)


head = ListNode(1, None)
head.next = ListNode(2, None)
head.next.next = ListNode(3, None)
head.next.next.next = ListNode(4, None)
head.next.next.next.next = ListNode(5, None)


driver = Solution()
driver.reverseList(head)

