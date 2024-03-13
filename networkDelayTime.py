class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

    #Djikstra
        def bfs(source):
            heapq.heappush(heap, (0, source))
            while heap:
                curr_time, curr_node = heapq.heappop(heap)
                visited.add(curr_node)

                if len(visited) == n:
                    return curr_time

                for time, neighbour in graph[curr_node]:
                    if neighbour not in visited:
                        heapq.heappush(heap, (curr_time + time, neighbour))

            return -1            


        graph = defaultdict(list)
        visited = set()


        for src, des, time in times:
            graph[src].append((time, des))

        heap = []           
        return bfs(k)


    # floyd Warshall

        graph = [[float("inf")]*n for _ in range(n)]

        for i in range(n):
            graph[i][i] = 0

        for src, des, time in times:
            graph[src-1][des-1] = time

        for alt in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][alt] + graph[alt][j])
        

        res = max(graph[k-1])
        return res if res != float("inf") else -1
