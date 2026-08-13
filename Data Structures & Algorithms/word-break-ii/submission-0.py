from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @cache
        def f(i):
            if i == N: return [[]]

            ret = []
            for l in range(1, L + 1):
                w = s[i: i + l]
                if w in wordDict:
                    for ans in f(i + l):
                        ret.append([w] + ans)
                
                if i + l == N:
                    break
            return ret

        N = len(s)
        wordDict = set(wordDict)
        L = max(len(w) for w in wordDict)
        res = f(0)
        return [" ".join(ans) for ans in res]
