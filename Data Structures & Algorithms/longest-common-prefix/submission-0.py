class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs = sorted(strs)
        if len(strs[len(strs)-1]) == 0:
            return prefix
        i = 1
        for c,c1 in zip(strs[len(strs)-1], strs[0]):
            if c != c1:
                return prefix
            prefix = strs[0][:i]
            i += 1
        return prefix