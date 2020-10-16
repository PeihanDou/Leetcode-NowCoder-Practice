
'''
一个数组，每个数决定了要向右跳几步（负数就是向左跳）
求数组里有没有环（必须一个方向，长度大于等于2）

'''
def circularArrayLoop(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        n = len(nums)
        for i, num in enumerate(nums):
            # 如果有环，以起点标识不同的环
            mark = str(i)
            
            while type(nums[i]) == int and num * nums[i] > 0 and nums[i] % n != 0:
                jump = nums[i]
                # 把同一个环都标为mark
                nums[i] = mark
                i = (i + jump) % n
            
            if nums[i] == mark:
                return True
        
        return False