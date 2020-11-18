'''
一个环长度为n，标号为0到n-1，从0开始，每数m个拿出一个，求最后剩下的标号
例如：
n=5，m=3
0，1，2，3，4
0，1，3，4
1，3，4
1，3
3
'''
## 公式法
# f(n,m) = (m%n + f(n-1,m)) % n = (m + f(n-1,m)) % n
# 由于f(n,m)代表从0开始过程，剩下的那个数
# 考虑过程的第一次，数到m%n,那么剩下的n-1个数继续这个过程，留下的会是f(n-1,m)，然而因为是从m%n开始数的， 所以留下的应该是(m%n + f(n-1, m))%n
def LastRemaining_Solution(self, n, m):
    # write code here
    if n <= 0: return -1
    f = 0
    for i in range(2,n+1):
        f = (f + m)%i
    return f

# 环形链表法 简单 空间复杂度不为1
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def LastRemaining_Solution1(n, m):
    # write code here
    head = ListNode(0)
    node = head
    for i in range(1, n):
        node.next = ListNode(i)
        node = node.next
    node.next = head
    k = 0
    while node.next!= node:
        k += 1
        print(k)
        if k == m:
            node.next = node.next.next
            k = 0
        else:
            node = node.next
    return node.val

