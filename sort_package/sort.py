n = [5,3,2,6,4,1]

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
        if l[0] > r[0]:
            m.append(r.pop(0))
        else:
            m.append(l.pop(0))
    if l:
        m += l
    if r:
        m += r
    return m

def quicksort(nums, l, h):
    if l < h:
        p = partition(nums, l, h)
        quicksort(nums, l, p-1)
        quicksort(nums, p+1, h)
    return nums
    
def partition(nums, l, h):
    pivot = nums[h]
    i = l-1
    # 保证i之前的都是比pivot小的
    for j in range(l, h):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        
    nums[h], nums[i+1] = nums[i+1], nums[h]
    return i+1

def heapsort(n):
    n = buildMaxheap(n)
    l = len(n)-1
    
    for i in range(len(n)-1, -1, -1):
        n[i], n[0] = n[0], n[i]
        l -= 1
        n = heapify(n, 0, l)
    return n

def heapify(n, i, length): # 上浮
    left = n[2*i+1] if 2*i+1 <length else float('-inf')
    right = n[2*i+2] if 2*i+2 <length else float('-inf')
    if n[i] < left or n[i] < right:
        h_id = 2*i+1 if left > right else 2*i+2
        n[h_id], n[i] = n[i], n[h_id]
        heapify(n, h_id, length)
    return n

def buildMaxheap(n):
    for i in range(len(n)//2, -1, -1):
        n = heapify(n, i, len(n))
    return n


    
# test
print(n)
print(mergesort(n))