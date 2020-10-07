def search(nums, target):
        l,h = 0, len(nums)-1
        if l == h:
            return nums[0] == target
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target: return True
            # 这个时候mid到h再到l是都相等的，判断会出问题，应移动l使得nums[l]!=nums[mid]为止。
            while l < mid and nums[l] == nums[mid]: # tricky part
                l += 1
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    h = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] < target <= nums[h]:
                    l = mid+1
                else:
                    h = mid-1
        return False