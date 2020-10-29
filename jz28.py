'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# 遍历数组，不相同的数对消去，剩下的数要么就是多出来的数，要么就是出现次数大于一半的数，再遍历即可
def MoreThanHalfNum_Solution(self, numbers):
    # write code here
    cond = -1
    cnt = 0
    for num in numbers:
        if cnt==0: # 不一样的数对已经全部消去
            cond = num
            cnt += 1
        else:
            if cond == num:
                cnt += 1
            else:
                cnt -= 1
    cnt = 0
    for num in numbers:
        if num == cond: cnt += 1
        if cnt > len(numbers)//2: return cond
    return 0