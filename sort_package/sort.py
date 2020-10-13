n = [1,4,2,5,7,6,3,4,8,7,4,6,9]

def switch_sort(nums):
    for i in range(len(nums)-1):
        for j in range(0,len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def insert_sort(nums):
    for i in range(1,len(nums)):
        cur = nums[i]
        pre_id = i-1
        while pre_id >= 0 and nums[pre_id] > cur:
            nums[pre_id+1] = nums[pre_id]
            pre_id -= 1
        nums[pre_id+1] = cur
    return nums

def select_sort(nums):
    
    for i in range(len(nums)):
        min_id = i
        for j in range(i, len(nums)):
            if nums[min_id] > nums[j]:
                min_id = j
        nums[i], nums[min_id] = nums[min_id], nums[i]
    return nums

def mergesort(nums):
    if len(nums) < 2:
        return nums
    mid = len(nums)//2
    l = nums[:mid]
    r = nums[mid:]
    return merge(mergesort(l), mergesort(r))

def merge(l, r):
    m = []
    while len(l) and len(r):
        if l[0] < r[0]:
            m.append(l.pop(0))
        else:
            m.append(r.pop(0))
    if l:
        m += l
# test
print(select_sort(n))