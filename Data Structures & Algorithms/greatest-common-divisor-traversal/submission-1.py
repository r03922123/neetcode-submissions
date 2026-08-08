import math


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def find(u):
            while root.setdefault(u, u) != u:
                root[u] = root[root[u]]
                u = root[u]
            return u

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv: return 
            root[ru] = rv
        
        A = set(nums)
        if 1 in A: return len(nums) == 1

        root = {a: a for a in A}
        # for a in sorted(A):
        #     for x in range(2, int(math.sqrt(a)) + 1):
        #         if a % x == 0:
        #             union(a, x)
        #             union(a, a//x)
        max_num = max(A)
        for x in range(2, int(math.sqrt(max_num)) + 1):
            for a in range(x * x, max_num + 1, x):
                if a in A:
                    union(a, x)
                    union(a, a//x)

        return len(set(find(a) for a in A)) == 1