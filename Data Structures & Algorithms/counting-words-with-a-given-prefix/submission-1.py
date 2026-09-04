
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n,res = len(pref),0
        for w in words:
            if len(w)<len(pref):
                continue
            inc =1
            for i in range(n):
                if w[i] !=pref[i]:
                    inc = 0
                    break
            res+=inc
        return res