class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 反转链表方法
def printListFromTailToHead(listNode):
        # write code here
        if not listNode: return []
        pre = None
        cur = listNode.next
        print(cur.val)
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        res = []
        while pre:
            res.append(pre.val)
            pre = pre.next
        return res

# 递归方法
def printListFromTailToHead1(listNode):
        # write code here
        res = []
        if not listNode:
            return res
        res = printListFromTailToHead1(listNode.next)
        if listNode.val != None:
            res.append(listNode.val)
        return res


a = [1,2,3,4]
list = ListNode(None)
head = list
for i in a:
    head.next = ListNode(i)
    head = head.next

cur = list.next
while cur:
    print(cur.val)
    cur = cur.next

print(printListFromTailToHead(list))