from collections import deque


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        N = len(words)
        graph = {}
        deg = {c: 0 for c in set(list("".join(words)))}
        for i in range(N-1):
            s1, s2 = words[i], words[i + 1]
            m, n = len(s1), len(s2)
            for k in range(m):
                if k == n: return ""
                if s1[k] != s2[k]:
                    if s2[k] not in graph.setdefault(s1[k], set()):
                        graph[s1[k]].add(s2[k])
                        deg[s2[k]] += 1
                    break

        queue = deque(c for c, d in deg.items() if d == 0)
        res = []
        while queue:
            u = queue.popleft()
            res.append(u)
            for v in graph.get(u, []):
                deg[v] -= 1
                if deg[v] == 0:
                    queue.append(v)
        
        return "".join(res) if len(res) == len(deg) else ""

    

                
