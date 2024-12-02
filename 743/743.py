import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):

        # Construcão do grafo
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Fila de prioridade
        pq = [(0, k)]
        distances = {i: float('inf') for i in range(1, n+1)} 
        distances[k] = 0

        while pq:
            current_dist, node = heapq.heappop(pq)

            if current_dist > distances[node]:
                continue

            # Atualiza vizinhos
            for neighbor, weight in graph[node]:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        # Verifica a maior distânci
        max_distance = max(distances.values())
        return max_distance if max_distance < float('inf') else -1
