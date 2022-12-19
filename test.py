class Solution(object):
    def insert(self, intervals, newInterval):
        ans = []
        for interval in intervals:
            if newInterval[0] > interval[1]: # head
                ans.append(interval)
            elif newInterval[1] < interval[0]: #tail
                ans.append(newInterval)
                newInterval = interval
            else: # merge
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
            print(newInterval)
        ans.append(newInterval) # last
        return ans
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
Solution().insert(intervals, newInterval)