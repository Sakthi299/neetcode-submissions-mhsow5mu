from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # given no.of nodes and edgelist
        # convert edgelist to adjacency list
        # visited set to detect loop
        
        
        adjlist = { i:[] for i in range(n)}
        for n1, n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)

        visited = set()
        """
        #RECURSIVE DFS
        def dfs(node, parent):
            if node in visited: # detect cycle
                return False

            visited.add(node)   
            for neigh in adjlist[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False
            
            return True

        return dfs(0, -1) and n == len(visited)
        """

        # ITERATIVE BFS
        # adjlist
        def bfs(node, parent):
            q = deque([(node, parent)])
            
            while q:
                node, parent = q.popleft()
                visited.add(node)
                #print(visited)
                for neigh in adjlist[node]:
                    if neigh == parent:
                        continue
                    if neigh in visited:
                        return False
                    q.append((neigh, node))

            return True
            
        return bfs(0, -1) and n == len(visited)






