'''
输入两个链表，找出它们的第一个公共结点。
（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
'''
# 假设两个链表长度为a和b，那么a不一定等于b，但是a+b=b+a，所以两个指针遍历到表尾的时候指向另一个表的表头
# 这样最终就会同时指向表尾，如果有共同节点那么就会返回
def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1
