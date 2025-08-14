class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for n in freq:
            buckets[freq[n]].append(n)

        res = []
        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) >= k:
                    return res
        return res
# NOTE: Uses bucket sort
