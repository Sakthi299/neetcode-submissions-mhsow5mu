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





