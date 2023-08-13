# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2):
        reminder = 0
        result_head = None
        last_node = None;
        while l1 is not None or l2 is not None:

            _sum = l1.val + l2.val + reminder;
            reminder = 0;
            if _sum > 9:
                reminder = int(_sum / 10)
                _sum = _sum % 10

            result = ListNode(_sum)

            if result_head is None:
                result_head = result
                last_node = result_head;
            else:
                last_node.next = result;
                last_node = last_node.next;

            if l1.next is None and l2.next is not None:
                l1.next = ListNode(0)

            if l1.next is not None and l2.next is None:
                l2.next = ListNode(0)

            l1 = l1.next
            l2 = l2.next
        if reminder > 0:
            last_node.next = ListNode(reminder)
        return result_head


# test case 1
def test_case_1():
    service = Solution()
    head1 = ListNode(2)
    e1 = ListNode(4)
    e2 = ListNode(3)
    head1.next = e1;
    e1.next = e2;

    head2 = ListNode(5)
    f1 = ListNode(6)
    f2 = ListNode(4)

    head2.next = f1
    f1.next = f2;
    res = service.addTwoNumbers(head1, head2)
    while res is not None:
        print(res.val, end=",")
        res = res.next
    print()

# test case 2
def test_case_2():
    service2 = Solution()
    t2_head1 = ListNode(5)
    t2_head2 = ListNode(5)
    res2 = service2.addTwoNumbers(t2_head1, t2_head2)

    while res2 is not None:
        print(res2.val, end=",")
        res2 = res2.next


test_case_1()
test_case_2()
