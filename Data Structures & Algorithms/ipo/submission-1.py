from heapq import heappush, heappop


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        n = len(profits)
        I = sorted(range(n), key=lambda i: capital[i])
        i = 0
        pq = []
        for _ in range(k):
            while i < n and capital[I[i]] <= w:
                heappush(pq, -profits[I[i]])
                i += 1
            
            if pq:
                w -= heappop(pq)
            else:
                break
        
        return w
            