from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr.lower() == 'none':
        return None
    list_repr = list_repr.split(' -> ')
    head = Node(int(list_repr[0]))
    node = head
    for el in list_repr[1:-1]:
        node.next = Node(int(el))
        node = node.next
    return head
