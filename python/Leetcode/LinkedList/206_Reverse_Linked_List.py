# Definition for singly-linked list.
from typing import Optional

# curr = head
# prev = None
# while curr:
#     nxt = curr.next
#     curr.next = prev
#     prev = curr
#     curr = nxt

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        print('-------')
        while prev is not None:
            print(prev.val)
            prev = prev.next




head = ListNode(1, None)
head.next = ListNode(2, None)
head.next.next = ListNode(3, None)
head.next.next.next = ListNode(4, None)
head.next.next.next.next = ListNode(5, None)


driver = Solution()
driver.reverseList(head)

