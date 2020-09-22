# 带回溯的dfs

# 递归前，判断终止条件：
# 如果s1，s2在字典里，那么直接返回dic[(s1,s2)]
# 如果s1=s2，那么返回True,dic更新
# 如果s1和s2长度不相等，或者字母频率不一样，则必然False，字典更新

# 进入递归：
# 对每一个位置把数组分为两块，如果是scramble的，那么这两块要么换了顺序，要么没换顺序
# 没换顺序，则应有s1[:i] = s2[:i], s1[i:]=s2[i:]
# 换了顺序的话，则s1[:i] = s2[-i:], s1[i:] = s2[:-i]
#以上两种可能有一种为真，则返回真

#出递归：
# 意味着每一个位置都不能把s1,s2分割为scramble的，那么s1,s2不为scramble， 返回False， 更新字典
class Solution:
    def __init__(self):
        self.dic = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.dic: return self.dic[(s1,s2)]
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            self.dic[(s1,s2)] = False
            return False
        if s1 == s2:
            self.dic[(s1,s2)] = True
            return True
        for i in range(1,len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or\
                (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
            
        self.dic[(s1,s2)] = False
        return False