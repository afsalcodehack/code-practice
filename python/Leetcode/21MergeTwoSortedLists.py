from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val > curr2.val:
                temp = curr2
                curr2 = curr2.next

                prev.next = temp
                temp.next = curr1
            else:
                prev = curr1
                curr1 = curr1.next
        if curr1 is None:
            prev.next = curr2

        while list1:
            print(list1.val)
            list1 = list1.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
list2.next.next = ListNode(10)

driver = Solution()
driver.mergeTwoLists(list1, list2)
