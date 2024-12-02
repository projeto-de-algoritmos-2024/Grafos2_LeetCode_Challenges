import heapq

class Solution:
    def minimumObstacles(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        pq = []
        
        heapq.heappush(pq, (0, 0, 0))  # (custo, x, y)
        
        while pq:
            cost, x, y = heapq.heappop(pq)
            
            if x == m - 1 and y == n - 1:
                return cost
            
            if visited[x][y]:
                continue
            visited[x][y] = True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(pq, (cost + grid[nx][ny], nx, ny))
                    
        return -1
