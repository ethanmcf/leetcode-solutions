class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)

        max_length = 1
        for num in nums:
            if num - 1 not in nums:
                count = 0
                temp = num
                while temp in nums:
                    count += 1
                    temp = temp + 1
                max_length = max(max_length, count)
        return max_length

"""
NOTES
Finds num where n-1 is not in nums, meaning we found the start of a consectutive sequence
O(n) since we iterate at most O(2n)
"""
