'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
'''
# if else时要先处理简单的情况：可以直接判断没有重叠的，直接append进res
# 有重叠时，更新n
def insert(intervals, newInterval):
    res = []
    n = newInterval
    for idx, i in enumerate(intervals):
        if n[1] < i[0]:
            res.append(n)
            return res + intervals[idx:]
        elif i[1] < n[0]:
            res.append(i)
        else:
            n[0] = min(n[0], i[0])
            n[1] = max(n[1], i[1])
    res.append(n)
    return res