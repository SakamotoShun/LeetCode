tempSortedList, sortedList = None, None
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    temp = ListNode(l1.val)
                    l1 = l1.next
                else:
                    temp = ListNode(l2.val)
                    l2 = l2.next                    
            elif l1:
                temp = ListNode(l1.val)
                l1 = l1.next
            else:
                temp = ListNode(l2.val)
                l2 = l2.next
            if sortedList:
                sortedList.next = temp
                sortedList = sortedList.next
            else:
                tempSortedList = sortedList = temp
        return tempSortedList