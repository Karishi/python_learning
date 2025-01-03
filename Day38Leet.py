# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    node = head
    count = 0
    while node:
        node = node.next
        count += 1
    while k >= count:
        k -= count
    index = count - k
    node = head
    for i in range(index-1):
        node = node.next
        new_links = node.next
    node.next = None
    new_head = new_links
    while new_links.next:
        new_links = new_links.next
    new_links.next = head
    return new_head

        

node5 = ListNode(50)
node4 = ListNode(40, node5)
node3 = ListNode(30, node4)
node2 = ListNode(20, node3)
node1 = ListNode(10, node2)

node = node1
while node:
    print(node.val)
    node = node.next

print()
new_head = rotateRight(node1, 8)
node = new_head
while node:
    print(node.val)
    node = node.next