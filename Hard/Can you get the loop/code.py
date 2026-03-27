def loop_size(node):
    slow = node
    fast = node
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    size = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        size += 1
    return size
