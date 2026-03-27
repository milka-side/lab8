from preloaded import Node

def swap_pairs(head):
    if head is None or head.next is None:
        return head
    node = Node()
    node.next = head
    cur = node
    while cur.next is not None and cur.next.next is not None:
        first = cur.next
        second = first.next
        cur.next = second
        first.next = second.next
        second.next = first
        cur = first
    return node.next
