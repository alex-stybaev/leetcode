class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        increment_next = False
        l1_exhausted = False
        l2_exhausted = False

        result = ListNode(0)
        head = result
        count = 0
        while 1:
            count += 1
            current_result = 0
            if not l1_exhausted:
                current_result += l1.val
            if not l2_exhausted:
                current_result += l2.val
            if increment_next:
                current_result += 1
                increment_next = False

            if current_result >= 10:
                current_result -= 10
                increment_next = True

            if l1_exhausted and l2_exhausted:
                break

            result.next = ListNode(current_result)
            result = result.next

            if l1.next is None:
                l1_exhausted = True
            else:
                l1 = l1.next
            if l2.next is None:
                l2_exhausted = True
            else:
                l2 = l2.next
            if l1_exhausted and l2_exhausted and increment_next:
                count += count
                result.next = ListNode(1)
                result = result.next
                break

        if count > 1:
            head = head.next

        return head


s = Solution()

l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)

l1.next = l2
l2.next = l3

# l4.next = l5
# l5.next = l6

print(s.add_two_numbers(l4, l4))