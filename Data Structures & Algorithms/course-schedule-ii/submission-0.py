class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
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

        



