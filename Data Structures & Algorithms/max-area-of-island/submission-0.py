class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r == rows or r < 0 or c == cols or c < 0 or grid[r][c] == 0 or (r,c) in visit):
                return 0
            visit.add((r ,c))
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))

        area = 0
        for i in range(rows):
            for j in range(cols):
                area = max(area, dfs(i, j))
        return area