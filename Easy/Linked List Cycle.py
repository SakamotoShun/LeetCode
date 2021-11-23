behind = front = head
while front and front.next:
    behind, front = behind.next, front.next.next
    if behind is front:
        return True
return False