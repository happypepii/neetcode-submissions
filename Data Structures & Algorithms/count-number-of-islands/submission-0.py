class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        count = 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if grid[i][j] != '1':
                return
            if visited[i][j]:
                return

            visited[i][j] = True

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
            