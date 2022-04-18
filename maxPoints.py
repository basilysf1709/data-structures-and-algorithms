from statistics import mode
import sys
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        if len(points) == 2:
            return 2
        maxPoints = {}
        for i, a in enumerate(points):
            j = 0
            count = 0
            slope = []
            while j < len(points):
                if i == j:
                    j += 1
                    continue
                if not (a[0] - points[j][0]) == 0:
                    tmpSlope = ((a[1] - points[j][1]) / (a[0] - points[j][0]))
                    slope.append(tmpSlope)
                else:
                    slope.append(sys.float_info.max)
                j += 1
            maxPoints[i] = slope
        count = 0
        l = 0
        while count < len(points):
            l = max(maxPoints[count].count(mode(maxPoints[count])), l)
            count += 1
        return l + 1