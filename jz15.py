import LinkedList

def ReverseList(pHead):
        # write code here
        if not pHead: return []
        pre = None
        cur = pHead
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

a = [1,2,3,4,5]
al = LinkedList.makeLinkedList(a)
al = ReverseList(al)
print(LinkedList.printLinkedList(al))


