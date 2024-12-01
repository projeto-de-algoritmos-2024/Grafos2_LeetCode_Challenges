import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, k)] 
        distances = {i: float('inf') for i in range(1, n+1)}
        distances[k] = 0
        visited = set() 

        while pq:
            current_dist, node = heapq.heappop(pq)

            if node in visited:
                continue
            visited.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    new_dist = current_dist + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))

        max_distance = max(distances.values())
        return max_distance if max_distance < float('inf') else -1
