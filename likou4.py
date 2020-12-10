'''

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
'''

def findMedianSortedArrays(nums1, nums2):
        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    # 第一个数组为空，直接返回第2个数组的第k大
                    return nums2[index2 + k - 1]
                if index2 == n:
                    # 第二个数组为空，直接返回第1个数组的第k大
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                # 正常情况
                # 选择两个数组里没有被排出的数里的第k//2 - 1个（或者最后一个）
                newIndex1 = min(index1 + k // 2 - 1, m - 1)
                newIndex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    # pivot1之前的都排除，排除了newIndex1 - index1 + 1个
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    # pivot2之前的都排除，排除了newIndex2 - index2 + 1个
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1
        
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2