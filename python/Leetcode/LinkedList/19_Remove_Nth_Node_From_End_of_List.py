from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(None)
        dummy.next = head
        left = dummy
        right = head

        for i in range(n):
            right = right.next

        while right:
            right = right.next
            left = left.next

        temp = left.next
        left.next = temp.next

        curr = dummy.next
        while curr:
            print(curr.val)
            curr = curr.next

head = ListNode(1, None)
head.next = ListNode(2, None)
# head.next.next = ListNode(3, None)
# head.next.next.next = ListNode(4, None)
# head.next.next.next.next = ListNode(5, None)
# head.next.next.next.next.next = ListNode(6, None)

driver = Solution()
driver.removeNthFromEnd(head, 2)
