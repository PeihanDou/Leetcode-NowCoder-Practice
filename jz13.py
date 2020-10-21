'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

'''

# time O(N^2), space O(1)
def reOrderArray(array):
        # write code here
        odd_id = 0
        for j in range(len(array)):
            if array[j] % 2 != 0:
                temp = array[j]
                for k in range(j-1, odd_id-1, -1):
                    print(k)
                    array[k+1] = array[k]
                array[odd_id] = temp
                odd_id += 1
a = [1,2,3,4,5,6,7]
reOrderArray(a)
print(a)