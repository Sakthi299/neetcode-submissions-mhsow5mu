class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)]
        rnk = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rnk[p2] > rnk[p1]:
                par[p1] = p2  
                rnk[p2] += rnk[p1] # rank/size of smaller tree added to larger tree
            else:
                par[p2] = p1
                rnk[p1] += rnk[p2]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res

        """
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
        """


        