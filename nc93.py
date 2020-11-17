'''
设计和构建一个“最近最少使用”缓存，该缓存会删除最近最少使用的项目。
缓存应该从键映射到值(允许你插入和检索特定键对应的值)，并在初始化时指定最大容量。
当缓存被填满时，它应该删除最近最少使用的项目。

它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class ListNode:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity):
        self.dict={}
        self.head=ListNode()
        self.tail=ListNode()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0
        self.capcity=capacity
     
    def movetohead(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        node.prev=self.head
         
    def put(self,key,value):
        if key not in self.dict:
            node=ListNode(key,value)
            self.dict[key]=node
            node.next=self.head.next
            self.head.next.prev=node
            node.prev=self.head
            self.head.next=node
            if self.size==self.capcity:
                temp=self.tail.prev
                temp.next.prev=temp.prev
                temp.prev.next=temp.next
                self.dict.pop(temp.key)
            else:
                self.size+=1
        else:
            node=self.dict[key]
            node.value=value
            self.movetohead(node)
         
    def get(self,key):
        if key not in self.dict:
            return -1
        else:
            node=self.dict[key]
            self.movetohead(node)
            return node.value