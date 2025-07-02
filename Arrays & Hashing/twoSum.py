  def twoSum(self, nums: List[int], target: int) -> List[int]:
      pos_solu = {}
      for i in range(len(nums)):
          pos_solu[target - nums[i]] = i

      for i in range(len(nums)):
          if nums[i] in pos_solu and i != pos_solu[nums[i]]:
              return [i, pos_solu[nums[i]]]
