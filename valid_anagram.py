class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        hash_s = {}
        hash_t = {}

        for char in s:
            if char in hash_s:
                hash_s[char] += 1
            else:
                hash_s[char] = 1


        for char in t:
            if char in hash_t:
                hash_t[char] += 1
            else:
                hash_t[char] = 1

        return hash_s == hash_t