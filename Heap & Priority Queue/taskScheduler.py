class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        heap = []
        for key in freq.keys():
            count = freq[key]
            task = key
            heapq.heappush(heap, (-count, task))

        cycles = 0
        while len(heap) > 0:
            used = []
            cool_down = cycles + n + 1
            while cycles < cool_down and len(heap) > 0:
                count, task = heapq.heappop(heap)
                used.append((count + 1, task))
                cycles += 1

            for count, task in used:
                if -count > 0:
                    heapq.heappush(heap, (count, task))

            if len(heap) == 0:
                return cycles
            
            if cycles < cool_down:
                cycles = cool_down


        return cycles

"""
Order by freq
choose most feq to least feq for n cycles (ie cool down)
if no more to choose in cool down, add idle times
"""
