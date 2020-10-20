'''
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
从右上角开始
利用观察：正左边的元素比当前元素小，正下边的元素比当前元素大
'''
def Find(target, array):
    # write code here
        m,n = len(array), len(array[0])
        i,j = 0,n-1
        while i < m and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                i += 1
            elif array[i][j] > target:
                j -= 1
        return False

a = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(Find(7, a))