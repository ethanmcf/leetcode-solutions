class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def combinations(current, index, total):
            for i in range(index, len(candidates)):
                currSum = total + candidates[i]
                if currSum < target:
                    combinations(current + [candidates[i]], i, currSum)
                elif currSum == target:
                    results.append(current + [candidates[i]])

        combinations([], 0, 0)
        return results
