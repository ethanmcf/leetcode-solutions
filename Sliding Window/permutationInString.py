class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        count = {}
        for c in s1:
            count[c] = count.get(c, 0) + 1

        left = 0
        right = 0
        for right in range(len(s2)):
            cR = s2[right]

            while left < right and (s2[right] not in count or count[s2[right]] <= 0):
                if s2[left] in count:
                    count[s2[left]] += 1
                left += 1 
            
            if s2[right] in count:
                count[s2[right]] -= 1

            if all(val == 0 for val in count.values()):
                return True

        return all(val == 0 for val in count.values())

  """
  Format for sliding window:
  left pointer, and iterate one at a time
  Move left pointer while right is not valid (and update left metric) 
  then update right metrics
  check for valid
  """
  
