from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = list1
        curr2 = list2
        tail = dummy = ListNode()
        while curr1 and curr2:
            if curr1.val > curr2.val:
                tail.next = curr2
                curr2 = curr2.next
            else:
                tail.next = curr1
                curr1 = curr1.next
            tail = tail.next

        if curr1:
            tail.next = curr1
        if curr2:
            tail.next = curr2
        return dummy.next


        while dummy:
            print(dummy.val)
            dummy = dummy.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(15)

list2 = ListNode(1)
list2.next = ListNode(6)
list2.next.next = ListNode(7)
list2.next.next.next = ListNode(10)

driver = Solution()
driver.mergeTwoLists(list1, list2)
