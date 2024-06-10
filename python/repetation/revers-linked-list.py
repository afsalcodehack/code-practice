
class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Solution:

    def reverse(self, head):

        tail = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        return tail
    

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

driver = Solution()
rev = driver.reverse(head)

while rev:
    print(rev.val)
    rev= rev.next





        