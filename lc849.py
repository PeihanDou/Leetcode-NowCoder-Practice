##https://leetcode.com/problems/maximize-distance-to-closest-person/

##通过计算连续0的个数来决定坐在哪一组0的中间（或者坐在最两边）

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)//2)
        return max(ans, seats[:].index(1), seats[::-1].index(1))