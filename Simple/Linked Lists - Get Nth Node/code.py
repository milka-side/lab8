from preloaded import Node

def get_nth(node, index):
    if index < 0 or node is None:
        raise Exception
    for i in range(index):
        node = node.next
        if node is None:
            raise Exception
    return node
