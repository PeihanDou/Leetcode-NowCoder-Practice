class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def printLinkedList(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

def makeLinkedList(array):
    head = ListNode(None)
    list = head
    for i in array:
        head.next = ListNode(i)
        head = head.next
    return list.next