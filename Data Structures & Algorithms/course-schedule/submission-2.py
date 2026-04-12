from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # numCourses = 5    # 0,1,2,3,4
        # prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]] -> edge list

        # Kahn's Algorithm
        # BFS Traversal

        indegree = [0]*numCourses
        
        adjList = { i:[] for i in range(numCourses)}
        # [c,p] p->c
        for c, p in prerequisites:
            adjList[p].append(c)
            indegree[c] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            
        order = []
        while q:
            node = q.popleft()
            order.append(node)

            for p in adjList[node]:
                indegree[p] -= 1
                if indegree[p] == 0:
                    q.append(p)
        
        return len(order) == numCourses
        
        """
        0 -> 1,2
        1 -> 3,4
        2 -> []
        3 -> 4
        4 -> []
        
        hashmap = { i:[] for i in range(numCourses) }

        visited = set()
        for c, p in prerequisites:
            hashmap[c].append(p)

        def dfs(c):
            if c in visited:     # visited to detect loop in graph
                return False
            if hashmap[c] == []: # base case of [] to backtrack
                return True
            
            visited.add(c)
            for pre in hashmap[c]: # chcek for all prerequisite
                if not dfs(pre):   # only if all dfs call returns True, then only exits loop or else return False
                    return False
            visited.remove(c)      # remove from set as that path is clear of loop and we are switching to other path in graph
            hashmap[c] = []        # as that path is already checked, assign [] as its completed
            return True

        for c in range(numCourses):  # runs through all vertices as some nodes can be isolated without connection with other nodes
            if not dfs(c):
                return False
        return True
        """
        """
        # with visited set to 
        prereq = { i:[] for i in range(numCourses) }

        for c,p in prerequisites:
            prereq[c].append(p)
        
        visited = set()
        cycle = set()

        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            
            cycle.add(c)

            for pre in prereq[c]:
                if not dfs(pre):
                    return False
            cycle.remove(c)
            visited.add(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        """

