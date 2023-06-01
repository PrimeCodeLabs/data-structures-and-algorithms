# Inefficient version
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    nodes = []
    while head:
        nodes.append(head)
        head = head.next

    for i in range(0, len(nodes)-1, 2):
        nodes[i].val, nodes[i+1].val = nodes[i+1].val, nodes[i].val

    return nodes[0]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swap_pairs_efficient(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    prev_node = dummy
    prev_node.next = head

    while head and head.next:
        first_node = head
        second_node = head.next

        prev_node.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        prev_node = first_node
        head = first_node.next

    return dummy.next
'''
Comments:
In terms of time complexity, both solutions have a time complexity of O(N) where N is the number of nodes in the linked list as they both visit each node once.

The space complexity for the inefficient solution is also O(N) as we're storing all nodes in a list, whereas for the efficient solution, 
the space complexity is O(1) as it doesn't require additional space that scales with input size, making it more space-efficient.
'''