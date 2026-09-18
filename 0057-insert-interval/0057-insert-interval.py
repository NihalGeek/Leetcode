class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res=[]
        for interval in intervals:
            if interval[1]<newInterval[0]:
                res.append(interval)
            elif interval[0]>newInterval[1]:
                res.append(newInterval)
                newInterval=interval
            elif (interval[0]<newInterval[1]) or (interval[1]>=newInterval[0]):
                newInterval[0]=min(interval[0],newInterval[0])
                newInterval[1]=max(interval[1],newInterval[1])
        res.append(newInterval)
        return res
        