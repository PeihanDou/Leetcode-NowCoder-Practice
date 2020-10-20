'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.
'''
def findMin(nums):
        l,r = 0, len(nums)-1
        min_num = float('inf')
        while l < r:
            mid = (l+r)//2
            min_num = min(min_num, nums[mid])
            '''
            This means the right part is all same numbers, ser r so that ignore the duplicated number
            '''
            while r > mid and nums[r] == nums[mid]: # trick part
                r -= 1
            if nums[r] < nums[mid]: # first part in order
                l = mid + 1
            else: # second part in order
                r = mid
        return nums[l]
                