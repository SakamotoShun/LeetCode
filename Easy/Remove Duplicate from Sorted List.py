# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

head = [1,1,2]
cur = head

while cur is not None and cur.next is not None:
    if cur.val == cur.next.val:
        cur.next = cur.next.next
        continue
    cur = cur.next
print(cur)