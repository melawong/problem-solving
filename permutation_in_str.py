class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = {}  #ab
        s2_hash = {}  #ei

        if len(s1) > len(s2):
            return False

        for char in range(len(s1)):
            if s1[char] in s1_hash:
                s1_hash[s1[char]] += 1
            else:
                s1_hash[s1[char]] = 1

            if s2[char] in s2_hash:
                s2_hash[s2[char]] += 1
            else:
                s2_hash[s2[char]] = 1

        if s1_hash == s2_hash:
            return True

        left = 0
        right = len(s1) - 1

        while right < len(s2) - 1 :

            s2_hash[s2[left]] -= 1
            if s2_hash[s2[left]] == 0:
                del s2_hash[s2[left]]
            left += 1
            right += 1

            if s2[right] in s2_hash:
                s2_hash[s2[right]] += 1
            else:
                s2_hash[s2[right]] = 1

            if s1_hash == s2_hash:
                return True
        return False