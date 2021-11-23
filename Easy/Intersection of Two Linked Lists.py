temp = set()

if headA == None or headB == None:
    return None

listA = headA
listB = headB

while listB or listA:
    if listB:
        if listB not in temp:
            temp.add(listB)
        else:
            return listB
        listB = listB.next
    
    if listA:
        if listA not in temp:
            temp.add(listA)
        else:
            return listA
        listA = listA.next
return None