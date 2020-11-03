'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''


def FindNumsAppearOnce(array):
        # write code here
        n = 0
        for i in array:
            n ^= i
        # n是目标的两个数异或成的， 取其中最低位的1所在的位数
        # 那么这两个数的对应位必为1，0，以这个为分界，将原数组分为两个数组，再异或
        index = 1
        while index & n == 0:
            index = index << 1
        r1, r2 = 0,0

        for i in array:
            if i & index == 0:
                r1 ^= i
            else:
                r2 ^= i
            
        return [r1, r2]

a = [1,3,2,2,4,4,6,6]
print(FindNumsAppearOnce(a))