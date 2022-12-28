class Solution(object):
    def merge(self, intervals):
        if len(intervals)==0:
            return []
        sort_intervals = sorted(intervals, key=lambda x:x[0])
        res=[sort_intervals[0]]
        for interval in sort_intervals[1:]:
            if interval[0]<=res[-1][1]:
                res[-1][1]=max(interval[1],res[-1][1])
            res.append(intervals)
        return res
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
intervals = [[1,3],[2,6],[8,10],[15,18]]
Solution().merge(intervals)