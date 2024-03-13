class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[False] * numCourses for _ in range(numCourses)]
        output = []

        for i in range(numCourses):
            graph[i][i] = True

        for c1, c2 in prerequisites:
            graph[c1][c2] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    graph[i][j] = graph[i][j] or graph[i][k] and graph[k][j]
                

        for s, e in queries:
            output.append(graph[s][e])
        
        return output
        
