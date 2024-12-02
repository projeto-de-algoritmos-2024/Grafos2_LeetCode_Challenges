from heapq import heappush, heappop

class Solution:
    def secondMinimum(self, num_nodes, edges, travel_time, light_cycle):
       
        # Cria listta de adjacencia par o grafo
        graph = [[] for _ in range(num_nodes)]
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        
        # minimos
        shortest_time = [float('inf')] * num_nodes
        second_shortest_time = [float('inf')] * num_nodes
        shortest_time[0] = 0
        
        # prioridade
        queue = [(0, 0)]  
        
        while queue:
            curr_time, curr_node = heappop(queue)
            
           
            if curr_time > second_shortest_time[curr_node]:
                continue
            
            for neighbor in graph[curr_node]:
                
                wait_time = 0
                if (curr_time // light_cycle) % 2 == 1:  
                    wait_time = light_cycle - (curr_time % light_cycle)
                
                arrival_time = curr_time + travel_time + wait_time
                
                # Atualiza minimos
                if arrival_time < shortest_time[neighbor]:
                    second_shortest_time[neighbor] = shortest_time[neighbor]
                    shortest_time[neighbor] = arrival_time
                    heappush(queue, (arrival_time, neighbor))
                elif shortest_time[neighbor] < arrival_time < second_shortest_time[neighbor]:
                    second_shortest_time[neighbor] = arrival_time
                    heappush(queue, (arrival_time, neighbor))
        
        return second_shortest_time[num_nodes - 1]
