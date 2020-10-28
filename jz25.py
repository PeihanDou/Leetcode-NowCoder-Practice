class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import LinkedList

'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
另一个特殊指针random指向一个随机节点），请对此链表进行深拷贝，并返回拷贝后的头结点。
（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
def Clone(pHead):
    # write code here
    p1 = pHead
    p2 = pHead
    dic = {}
    while p1:
        dic[p1] = ListNode(p1.val)
        p1 = p1.next
    while p2:
        if p2.next != None:
            dic[p2].next = dic[p2.next]
        else:
            dic[p2].next = None
        # for test reason comment this line.
        # dic[p2].random = dic[p2.random]
        p2 = p2.next
    return dic[pHead]


a = [1,2,3,4,5]
a1 = LinkedList.makeLinkedList(a)
b1 = Clone(a1)
print(LinkedList.printLinkedList(b1))
