from preloaded import Node

def stringify(node):
    string = ''
    while node is not None:
        string += f'{node.data} -> '
        node = node.next
    string += 'None'
    return string
