class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        val = 1
        left, right, top, bottom = 0, n - 1, 0, n - 1
        while val <= n ** 2:
            for i in range(left, right + 1):
                res[top][i] = val
                val += 1
            for i in range(top + 1, bottom + 1):
                res[i][right] = val
                val += 1
            for i in range(right - 1, left - 1, -1):
                res[bottom][i] = val
                val += 1
            for i in range(bottom - 1, top, -1):
                res[i][left] = val
                val += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res
