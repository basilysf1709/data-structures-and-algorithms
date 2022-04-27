class Solution:
    def insertFirstAttempt(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) != 0 and newInterval[0] < intervals[0][0] and newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        nums = []
        flag = 0
        for interval in intervals:
            if newInterval[1] >= interval[0] and newInterval[0] <= interval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
                nums.append(newInterval) if newInterval not in nums else nums
                flag = 1
            else:
                nums.append(interval)
        if flag == 0:
                nums.append(newInterval)
                nums.sort(key=lambda x: x[0])
        return nums
    def insertYoutubeSolution(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        nums = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                nums.append(newInterval)
                return nums + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                nums.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        nums.append(newInterval)
        return nums