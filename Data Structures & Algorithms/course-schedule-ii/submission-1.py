from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0]*numCourses

        adjList = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            adjList[p].append(c)
            indegree[c] += 1

        q = deque()
        order = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            
        while q:
            node = q.popleft()
            order.append(node)

            for p in adjList[node]:
                indegree[p] -= 1
                if indegree[p] == 0:
                    q.append(p)
                
        if len(order) == numCourses:
            return order
        else:
            return []

        """
        #Adjacency List
        preReqMap = { i:[] for i in range(numCourses) } 

        for c, pre in prerequisites:
            preReqMap[c].append(pre)
        
        output = []
        # cycle to holds nodes during one path traversal
        # visited to hold finished nodes 
        visited, cycle = set(), set() 

        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True
            
            cycle.add(c)
            for pre in preReqMap[c]:
                if not dfs(pre):
                    return False

            # POST-ORDER TRAVERSAL LOGIC
            cycle.remove(c)
            visited.add(c)
            output.append(c)
            return True


        for c in range(numCourses):
            if not dfs(c):  # if false, then it detects cycle so returns []
                return []   

        return output
        """
        



