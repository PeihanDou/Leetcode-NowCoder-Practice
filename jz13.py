'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

# time O(N^2), space O(1)
def reOrderArray(array):
        # write code here
        odd_id = 0
        for j in range(len(array)):
            # 遍历数组，如果遇上奇数，则[odd_id:j]之间的数都往后移一格
            if array[j] % 2 != 0:
                temp = array[j]
                # 整体后移一位
                array[odd_id+1:j+1] = array[odd_id:j]
                array[odd_id] = temp
                odd_id += 1
a = [1,2,3,4,5,6,7]
reOrderArray(a)
print(a)