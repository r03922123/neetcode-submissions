class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru != rv:
                root[ru] = rv
                return True
            return  False

        def find(u):
            while root[u] != u:
                root[u] = root[root[u]]
                u = root[u]
            return u
        
        res = [[], []]
        root = list(range(n))
        E = len(edges)
        mst = 0
        idx = sorted(range(E),  key=lambda i: edges[i][2])
        for i in idx:
            u, v, w = edges[i]
            ru, rv = find(u), find(v)
            if ru != rv:
                root[ru] = rv
                mst += w

        for j in range(E):
            s = 0
            root = list(range(n))
            total = n
            for i in idx:
                if i == j: continue

                u, v, w = edges[i]
                if union(u, v):
                    s += w
                    total -= 1

            if total != 1 or s > mst:
                res[0].append(j)
                continue

            u, v, w = edges[j]
            root = list(range(n))
            s = w
            ru, rv = find(u), find(v)
            root[ru] = rv
            for i in idx:
                if i == j: continue

                u, v, w = edges[i]
                ru, rv = find(u), find(v)
                if union(u, v):
                    s += w

            if s == mst:
                res[1].append(j)                
        return res