# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        dummy = ListNode()
        dummy.next = head

        fast, slow = dummy, dummy

        while fast.next:
            fast = fast.next
            slow = slow.next
            if fast.next:
                fast = fast.next
            #print(slow.val, fast.val)

        #revers
        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        mid = prev
        curr = head
        while curr and mid:
            temp1 = curr.next
            temp2 = mid.next

            curr.next = mid
            mid.next = temp1

            curr = temp1
            mid = temp2

        while head:
            print(head.val)
            head = head.next


head = ListNode(1, None)
head.next = ListNode(2, None)
head.next.next = ListNode(3, None)
# head.next.next.next = ListNode(4, None)
# head.next.next.next.next = ListNode(5, None)
# head.next.next.next.next.next = ListNode(6, None)

driver = Solution()
driver.reorderList(head)
