from LinkedList import *

def addTwoNumbers(l1, l2):
    carry = 0
    p1 = l1
    p2 = l2
    ret = ListNode(0)
    cur = ret
    print(printLinkedList(ret))
    while p1 and p2:
        cur.next = ListNode((p1.val + p2.val + carry) % 10)
        if p1.val + p2.val + carry >= 10:
            carry = 1
        else:
            carry = 0
        cur = cur.next
        p1 = p1.next
        p2 = p2.next
        print(printLinkedList(ret))
    while p1:
        cur.next = ListNode((p1.val + carry) % 10)
        if p1.val + carry >= 10:
            carry = 1
        else:
            carry = 0
        cur = cur.next
        p1 = p1.next
    while p2:
        cur.next = ListNode((p2.val + carry) % 10)
        if p2.val + carry >= 10:
            carry = 1
        else:
            carry = 0
        cur = cur.next
        p2 = p2.next
    return ret.next

a = makeLinkedList([2,4,3])
b = makeLinkedList([5,6,4])
print(printLinkedList(addTwoNumbers(a, b)))