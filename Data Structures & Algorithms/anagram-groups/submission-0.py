class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # 
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

        """
        ok the logic here, 
        first thing we do create a hashmap where the key is
        gonna be the character count and the value is gonna be
        the string

        iterate thru the list of strings 
            to start have the count of each of the strings
            == 0 (times 26 for all the characters in the alph)

            iterate each character in the string
                go to characters index in count array 
                (ord(c) - ord('a')) and add 1

            append the string to the key of the count make 
            it a tuple bc python is stupid

        return all the values which ends up making the sub arrays
        """