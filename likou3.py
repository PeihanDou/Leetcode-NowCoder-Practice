'''
#############好题###########
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''

# 遍历一遍
# 字典存的是每个字符最新出现的下标
# 当出现重复时，先更新k，再更新c_dict[c]，这样k就指在第二新的重复字符上（即，k之后的窗口里只有一次这个字符）
def lengthOfLongestSubstring(s: str) -> int:
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res

# 遍历两边，滑动窗口
def lengthOfLongestSubstring1(s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans