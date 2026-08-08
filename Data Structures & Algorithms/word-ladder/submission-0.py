class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:return 0

        wordList.add(beginWord)
        p2w, w2p = {}, {}

        for w in wordList:
            for i in range(len(w)):
                p = w[:i] + "*" + w[i+1:]
                p2w.setdefault(p, []).append(w)
                w2p.setdefault(w, []).append(p)
        
        q1, q2 = set([beginWord]), set([endWord])
        step = 1
        q = set()
        wordList.remove(beginWord)
        wordList.remove(endWord)
        while q1 and q2:
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            
            for w in q1:
                for p in w2p[w]:
                    for v in p2w[p]:
                        if v in q2: return step + 1
                        if v in wordList:
                            wordList.remove(v)
                            q.add(v)
            q, q1 = q1, q
            q.clear()
            step += 1
        return 0