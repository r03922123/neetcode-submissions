class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # build relation graph
        # make sure there is no self loop
        # assign rows and columns from low degree, small index

        
        def assign(queue, coord, degree, graph):
            idx = 0
            while queue:
                for _ in range(len(queue)):
                    u = queue.popleft()
                    coord[u] = idx
                    for v in graph.get(u, []):
                        degree[v] -= 1
                        if degree[v] == 0:
                            queue.append(v)
                    
                    idx += 1
            return coord

        def build(conditions, k):
            graph = {}
            deg, coord = [0] * k, [-1] * k
            for u, v in conditions:
                graph.setdefault(u - 1, []).append(v - 1)
                deg[v - 1] += 1
                
            queue = deque(u for u in range(k) if deg[u] == 0)

            coord = assign(queue, coord, deg, graph)
            if sum(coord[u] != -1 for u in range(k)) != k: return []
            return coord
            
        row_coord = build(rowConditions, k)
        if not row_coord: return []

        col_coord = build(colConditions, k)
        if not col_coord: return []

        res = [[0] * k for _ in range(k)]
        for val, (row, col) in enumerate(zip(row_coord, col_coord)):
            res[row][col] = val + 1
        
        return res