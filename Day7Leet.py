# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        digit1 = l1[0]
        digit2 = l2[0]
        outputLL = []
        output = ListNode()
        carried = 0
        while digit1 is not None or digit2 is not None:
            if digit1 is None:
                digit1val = 0
            else:
                digit1val = digit1.val
            if digit2 is None:
                digit2val = 0
            else:
                digit2val = digit2.val
            output.val = (digit1val + digit2val + carried) % 10
            carried = (digit1val + digit2val + carried) // 10
            new_node = ListNode()
            output.next = new_node
            digit1 = digit1.next
            digit2 = digit2.next
            output = output.next
        if carried > 0:
            output.val = 1