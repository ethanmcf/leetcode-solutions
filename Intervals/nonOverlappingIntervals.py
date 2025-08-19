class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
            intervals.sort(key=lambda x: x[0])
            count = 0
            start, end = intervals[0]
            for i in range(1, len(intervals)):
                curr = intervals[i]
                if start <= curr[0] < end:
                    if end > curr[1]:
                        start, end = curr[0], curr[1]
                    count += 1
                else:
                    start, end = curr
                
            return count
# Uses lambda to increase speed
