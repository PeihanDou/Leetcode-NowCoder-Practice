'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.
'''
# 贪心算法
# 每一步都要把 从已有的可能停留的点开始跳的最靠前的地方 视为目前的cover
def jump(nums):
    cur_cover = 0
    last_jump = 0
    count = 0
    if len(nums) == 1: return 0
    for i in range(len(nums)):
        cur_cover = max(cur_cover, i + nums[i]) #这个节点前的所有节点（包含此节点），最远能跳到哪里？
        
        if i==last_jump: # 上一回最远能跳到这里，相等的时候，就必须再跳一次了，更新last_jump, count
            last_jump = cur_cover
            count += 1
            if last_jump >= len(nums)-1:
                return count
    return count