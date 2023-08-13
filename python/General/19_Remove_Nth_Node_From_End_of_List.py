class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        s = head
        f = head

        for i in range(0, n):
            f = f.next

        if f is None:
            return head.next

        while f.next:
            f = f.next
            s = s.next
        s.next = s.next.next
        return head



l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(6)
l.next.next.next.next.next.next = ListNode(7)
service = Solution()
head = service.removeNthFromEnd(l, 3)

node = head
while node:
    print(node.val)
    node = node.next
