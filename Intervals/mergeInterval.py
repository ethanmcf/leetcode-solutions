class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        res = []

        res.append(intervals[0])
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], curr[1])
            else:
                res.append(curr)

        return res
