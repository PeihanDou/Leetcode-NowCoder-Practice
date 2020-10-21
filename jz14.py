'''
输入一个链表，输出该链表中倒数第k个结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def FindKthToTail(head, k):
        # write code here
        cur = head
        l = 0
        while cur:
            l += 1
            cur = cur.next
        
        idx = l - k + 1
        cur = head
        l = 0
        while cur:
            l += 1
            if l == idx:
                return cur
            cur = cur.next


