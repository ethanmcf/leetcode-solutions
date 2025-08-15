class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        seen = [[0] * n for _ in range(m)]

        def dfs(si, sj, seen, grid):
            stack = [(si,sj)]
            while len(stack) > 0:
                i, j = stack.pop(-1)
                if seen[i][j] == 0 and grid[i][j] == '1':
                    seen[i][j] = 1
                    if i - 1 >= 0:
                        stack.append((i - 1, j))
                    if i + 1 < m:
                        stack.append((i + 1, j))
                    if j - 1 >= 0:
                        stack.append((i, j - 1))
                    if j + 1 < n:
                        stack.append((i, j + 1))
                    
        for i in range(m):
            for j in range(n):
                if seen[i][j] == 0 and grid[i][j] == '1':
                    dfs(i,j, seen, grid)
                    count += 1

        return count
# DFS
