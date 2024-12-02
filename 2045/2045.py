from collections import defaultdict, deque
from typing import List

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Construir o grafo
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque([(0, 1)])
        

        visited_times = {i: [] for i in range(1, n + 1)}
        visited_times[1].append(0)
        
        while queue:
            elapsed, node = queue.popleft()
            
            for neighbor in graph[node]:
                cycle = elapsed // change
                if cycle % 2 == 1:  
                    wait_time = (cycle + 1) * change - elapsed
                else:  
                    wait_time = 0
                
                new_time = elapsed + time + wait_time
                
                if len(visited_times[neighbor]) < 2:
                    visited_times[neighbor].append(new_time)
                    visited_times[neighbor].sort() 
                    queue.append((new_time, neighbor))
                elif new_time not in visited_times[neighbor] and new_time > visited_times[neighbor][0]:
                    visited_times[neighbor].append(new_time)
                    visited_times[neighbor].sort()
                    visited_times[neighbor] = visited_times[neighbor][:2]
                    queue.append((new_time, neighbor))
        
        return visited_times[n][1] if len(visited_times[n]) > 1 else -1