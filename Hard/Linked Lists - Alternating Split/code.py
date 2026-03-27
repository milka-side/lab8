class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception
    node = head
    first = Node()
    second = Node()
    cur1 = first
    cur2 = second
    while node is not None:
        cur1.next = node
        cur1 = cur1.next
        node = node.next
        if node is not None:
            cur2.next = node
            cur2 = cur2.next
            node = node.next
    cur1.next = None
    cur2.next = None
    return Context(first.next, second.next)
