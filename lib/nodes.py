import math

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def setNext(self, x):
        self.next = x

class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last_odd = head
        last_even = None
        current = head
        first_even = current.next
        first_odd = current
        count = 1

        if head.next == None:
            return head

        while (True):
            if (count%2 == 1):
                if (count != 1):
                    last_odd.next = current
                if current.next == None:
                    current.next = first_even
                    last_even.next = None
                    break
                last_odd = current
            else:
                if last_even != None:
                    last_even.next = current
                if current.next == None:
                    last_odd.next = first_even
                    break
                last_even = current
            current = current.next
            count += 1
        return first_odd

t1 = ListNode(1)
# t2 = ListNode(2)
# t3 = ListNode(3)
# t4 = ListNode(4)
# t1.setNext(t2)
# t2.setNext(t3)
# t3.setNext(t4)


s = Solution()
current = s.oddEvenList(t1)
while (current != None):
    print(vars(current))
    current = current.next