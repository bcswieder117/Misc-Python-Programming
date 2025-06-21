# Blaine Swieder
# LeetCode (Python): Critical Connections in a Network
# June 20th, 2025

from collections import defaultdict 

class Solution: 
    def criticalConnections(self, n, connections): 
        graph = defaultdict(list)
        for u, v in connections: 
            graph[u].append(v)
            graph[v].append(u) 
            
        disc = [-1] * n 
        low = [-1] * n 
        time = [0]
        res = [] 
        
        def dfs(u, parent): 
            disc[u] = low[u] = time[0] 
            time[0] += 1
            
            for v in graph[u]:
                if v == parent: 
                    continue
                if disc[v] == -1: 
                    dfs(v, u)
                    low[u] = min(low[u], low[v]) 
                    if low[v] > disc[u]: 
                        res.append([u, v])
                else: 
                    low[u] = min(low[u], disc[v])
                    
        dfs(0, -1)
        return res
    
    
####### Example ##############################################


sol = Solution()

# Example 1

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(sol.criticalConnections(n, connections))  # Expected output is [[1,3]]

# Example 2

n = 2
connections = [[0,1]]
print(sol.criticalConnections(n, connections))  # Expected output is [[0,1]]

