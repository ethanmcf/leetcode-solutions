class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            if n in self.memo:
                return self.memo[n]
            else:
                val = self.climbStairs(n - 1) + self.climbStairs(n - 2)
                self.memo[n] = val
                return val
