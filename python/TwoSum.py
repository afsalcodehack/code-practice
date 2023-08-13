class ListNode:
    def __init__(self):
        self.val = None
        self.next = None

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        reminder = 0
        result = ListNode(self)
        result_head = None
        last = None
        while l1 is not None or l2 is not None:
            _sum = l1.val + l2.val + reminder

            if _sum > 9:
                reminder = int(_sum / 10)
                _sum = _sum % 10

            result = ListNode(_sum)

            if result_head is None:
                result_head = result
            else:
                last = result_head
                while last.next is not None:
                    last = last.next
                last.next = result

            l1 = l1.next
            l2 = l2.next
        return result_head


# service = Solution()
# head1 = ListNode(2)
# e1 = ListNode(4)
# e2 = ListNode(3)
# head1.next = e1
# e1.next = e2
#
# head2 = ListNode(5)
# f1 = ListNode(6)
# f2 = ListNode(4)
# f3 = ListNode(3)

service = Solution()
head1 = ListNode(1)
e1 = ListNode(8)


head2 = ListNode(0)
f1 = ListNode(0)

head2.next = f1

res = service.addTwoNumbers(head1, head2)

while res is not None:
    print(res.val)
    res = res.next
