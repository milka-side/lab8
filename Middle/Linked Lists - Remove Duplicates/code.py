class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    node = head
    while node.next is not None:
        if node.data == node.next.data:
            node.next = node.next.next
            continue
        node = node.next
    return head
