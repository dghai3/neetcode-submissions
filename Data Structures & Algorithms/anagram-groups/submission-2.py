class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            lis = [0]*26
            for char in word:
                lis[ord(char) - ord('a')] += 1
            anagrams[tuple(lis)].append(word)
        return list(anagrams.values())
