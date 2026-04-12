class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjlist = { i:[] for i in range(n) }

        for n1, n2 in edges:
            adjlist[n1].append(n2)
            adjlist[n2].append(n1)
        
        visited = set()
        components = 0


        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in adjlist[node]:
                if neigh == parent:
                    continue
                dfs(neigh, node)
            
            return True
        

        for i in range(n):
            if dfs(i, -1):
                components += 1
        return components


        