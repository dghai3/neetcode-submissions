class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sLetters = {}
        tLetters = {}
        for i in range(len(s)):
            sLetters[s[i]] = sLetters.get(s[i], 0) + 1
            tLetters[t[i]] = tLetters.get(t[i], 0) + 1
        return sLetters == tLetters