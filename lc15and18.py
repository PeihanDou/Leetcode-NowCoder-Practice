# in an array find a+b+c=0. return all abc that satisfy.
def threeSum(self, nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):  #只扫描到倒数第三个，因为至少需要三个数
        if i > 0 and nums[i] == nums[i-1]: # 不考虑重复的
            continue
        l, r = i+1, len(nums)-1
        while l < r: #左右指针
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res


# 4sum, ksum general
def fourSum(nums, target):
    def ksum(nums, target, k):  #递归调用该函数
        res = []
        if len(nums)==0 or nums[0] * k > target or nums[-1] * k < target:#终止条件1：不可能找到和为target的情况
            return res
        if k==2:#终止条件2：简化为2sum的情况
            return twoSum(nums, target)
        for i in range(len(nums)):#递归调用
            if i == 0 or nums[i-1] != nums[i]:#防止重复
                for _, set in enumerate(ksum(nums[i+1:], target - nums[i], k-1)):
                    res.append([nums[i]] + set)
        return res
    def twoSum(nums, target):
        res = []
        l,h = 0, len(nums)-1
        while l < h:
            s = nums[l] +nums[h]
            if s < target or (l > 0 and nums[l] == nums[l-1]):
                l += 1
            elif s > target or (h <len(nums)-1 and nums[h] == nums[h+1]):
                h -= 1
            else:
                res.append([nums[l], nums[h]])
                l,h = l+1, h-1
        return res
    
    nums.sort()
    return ksum(nums, target, 4)