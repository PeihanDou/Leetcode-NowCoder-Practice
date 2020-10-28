'''
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''

# 用一个辅助栈模拟。具体地
# push[i] 与pop[j]比较，若不相等，说明没有立即出栈，放入模拟栈里
# 若相等，则i++,j++（说明入栈后立刻出栈）
# 这时比较模拟栈的栈顶和pop[j]，若相等则弹出，循环，否则进行下一步
# 直到遍历完push，此时若stack空则true，否则false
def IsPopOrder(self, pushV, popV):
    # write code here
    stack = []
    i,j = 0,0
    while i < len(pushV):
        if pushV[i] != popV[j]:
            stack.append(pushV[i])
            i += 1
        else:
            i += 1
            j += 1
            while stack and stack[-1] == popV[j]:
                stack.pop()
                j += 1
    return stack == []