'''
并查集算法
'''

class UnionSet():
    def __init__(self):
        self.parent = {}
    
    def init(self, key):
        if key not in self.parent:
            self.parent[key] = key

    # 普通查找
    def find(self, key):
        self.init(key)
        while self.parent[key] != key:
            key = self.parent[key]
        return key
    
    # 自带路径压缩的查找
    def find_squeeze(self, key):
        self.init(key)
        if self.parent[key] == key:
            return key
        self.parent[key] = self.find_squeeze(self.parent[key])
        
        return self.parent[key]
        
    def join(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return 
        self.parent[qroot] = proot
    
    def is_connect(self, p, q, squeeze=False):
        return self.find_squeeze(p) == self.find_squeeze(q) if squeeze else self.find(p) == self.find(q)

a = UnionSet()
a.init(1)
a.init(2)
a.init(3)
a.join(1,2)
a.join(3,2)
a.join(4,5)
a.join(5,7)
a.join(7,1)
print(a.is_connect(2,5, squeeze=False))
print('不带路径压缩',a.parent)
print(a.is_connect(2,5, squeeze=True))
print('带路径压缩',a.parent)
