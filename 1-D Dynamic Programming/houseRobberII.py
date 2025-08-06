class Solution:
    def rob(self, nums: List[int]) -> int:
        m1 = self.money(0, len(nums) - 1, nums)
        m2 = self.money(1, len(nums), nums)

        return max(m1, m2)

    def money(self, i, j, nums):
        if len(nums) == 1:
            return nums[0]
        maxv = 0
        prev_rob = 0

        for i in range(i,j):
            temp = max(maxv, prev_rob + nums[i])
            prev_rob = maxv
            maxv = temp
        return maxv
