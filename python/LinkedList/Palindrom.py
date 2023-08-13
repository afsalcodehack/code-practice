# Given a singly linked list, determine if it is a palindrome.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num = []
        i = 0
        while head is not None:
            num.append(head.val)
            head = head.next
        return num == num[::-1]


one = ListNode(-129)
two = ListNode(-129)
three = ListNode(1)
one.next = two
# two.next = three
print(Solution.isPalindrome(None, one))
