def sorted_insert(head, data):
    if head is None:
        return Node(data)
    if head.data > data:
        new_node = Node(data)
        new_node.next = head
        return new_node
    node = head
    prev = node
    while node is not None:
        if node.data > data:
            new_node = Node(data)
            prev.next = new_node
            new_node.next = node
            return head
        prev = node
        node = node.next
    prev.next = Node(data)
    return head
