import timeit

from solution import ListNode, swap_pairs, swap_pairs_efficient

def create_linked_list(n):
    """Creates a linked list with n nodes."""
    head = ListNode(1)
    current_node = head
    for i in range(2, n + 1):
        current_node.next = ListNode(i)
        current_node = current_node.next
    return head

n = 10000  # change as necessary
head = create_linked_list(n)

start_time = timeit.default_timer()
swap_pairs(head)
end_time = timeit.default_timer()
inefficient_time = end_time - start_time
print(f"Inefficient method took {inefficient_time} seconds.")

head = create_linked_list(n)  # recreate the linked list
start_time = timeit.default_timer()
swap_pairs_efficient(head)
end_time = timeit.default_timer()
efficient_time = end_time - start_time
print(f"Efficient method took {efficient_time} seconds.")

improvement = ((inefficient_time - efficient_time) / inefficient_time) * 100
print(f"The efficient method is {improvement}% faster than the inefficient method.")
