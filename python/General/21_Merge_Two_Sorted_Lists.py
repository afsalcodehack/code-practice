class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None: return l1

        if l1 is None and l2 is not None: return l2
        if l1 is not None and l2 is None: return l1

        if l1.val <= l2.val:
            new_list = ListNode(l1.val)
            l1 = l1.next
        else:
            new_list = ListNode(l2.val)
            l2 = l2.next

        head = new_list
        while l1 and l2:
            if l1.val <= l2.val:
                new_list.next = ListNode(l1.val)
                l1 = l1.next
            else:
                new_list.next = ListNode(l2.val)
                l2 = l2.next
            new_list = new_list.next

        if l1 is not None:
            new_list.next = l1
        if l2 is not None:
            new_list.next = l2

        return head


p1 = ListNode(1)
p1.next = ListNode(2)
p1.next.next = ListNode(4)
p1.next.next.next = ListNode(7)

p2 = ListNode(1)
p2.next = ListNode(3)
p2.next.next = ListNode(4)
p2.next.next.next = ListNode(5)

service = Solution()
head = service.mergeTwoLists(p1, p2)


while head:
    print(head.val)
    head = head.next
