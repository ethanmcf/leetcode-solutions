class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permutations(current, used):
            if len(current) == len(nums):
                result.append(current)
                return 
            for i in range(0, len(nums)):
                if i not in used:
                    used.add(i)
                    permutations(current + [nums[i]], used)
                    used.remove(i)
                    
        permutations([], set())
        return result
