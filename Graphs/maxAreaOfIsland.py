class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        maxArea = 0
        
        def dfs(row, col):
            curArea = 0
            stack = [(row, col)]
            while len(stack) > 0:
                i, j = stack.pop()
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                    if not visited[i][j] and grid[i][j]:
                        curArea += 1
                        stack.extend([(i - 1, j),(i + 1, j),(i, j - 1),(i, j + 1)])
                        visited[i][j] = 1
            return curArea

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]:
                    curArea = dfs(i, j)
                    maxArea = max(maxArea, curArea)
        return maxArea
