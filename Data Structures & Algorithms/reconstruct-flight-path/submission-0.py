class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def f(u):
            while graph.get(u, []):
                v = graph[u].pop()
                f(v)
            res.append(u)

        graph = {}
        for u, v in tickets:
            graph.setdefault(u, []).append(v)
        for v in graph.values():
            v.sort(reverse=True)
        
        res = []
        f("JFK")
        return res[::-1]