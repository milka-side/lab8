from preloaded import Node

def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    head = None
    for i in range(3, 0, -1):
        node = push(head, i)
        head = node
    return node
