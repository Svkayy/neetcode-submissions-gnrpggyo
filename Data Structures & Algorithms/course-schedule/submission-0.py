from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        path = set()
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True
            
            path.add(course)
            visited.add(course)

            for b in graph[course]:
                if not dfs(b):
                    return False

            path.remove(course)

            return True
        
        for val in list(graph.keys()):
            if not dfs(val):
                return False
        
        return True
            