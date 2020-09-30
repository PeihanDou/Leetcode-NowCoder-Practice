# https://leetcode.com/problems/house-robber-ii/ house robber II
# https://leetcode.com/problems/house-robber/    house robber

def rob(self, nums):
    if len(nums)<=3:
        return max(nums) if nums else 0
    dp1 = [0] * (len(nums)-1)
    dp2 = [0] * (len(nums)-1)
    dp1[0] = nums[0]
    dp1[1] = max(nums[:2])
    dp2[0] = nums[1]
    dp2[1] = max(nums[1:3])
    for i in range(2, len(nums)-1):
        dp1[i] = max(dp1[i-1], nums[i]+dp1[i-2])
        dp2[i] = max(dp2[i-1], nums[i+1]+dp2[i-2])
    return max(dp1[-1], dp2[-1])


# 简化，空间O(1)，时间O(n)
def rob2(self, nums):
    def simple_rob(num, i, j):
        f1, f2 = 0,0
        for k in range(i,j): f1, f2 = f2, max(f1+num[k], f2)
        return max(f1,f2)
    if len(nums)<= 3:
        return max(nums) if nums else 0
    return max(simple_rob(nums, 0, len(nums)-1), simple_rob(nums, 1, len(nums)))