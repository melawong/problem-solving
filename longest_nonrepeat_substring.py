class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        max_substring =  0
        letter_hash = {}

        start = 0
        end = 0

        while end < len(s):
            if s[end] not in letter_hash:
                letter_hash[s[end]] = 1
                end += 1
            else:
                letter_hash[s[end]] += 1
                while letter_hash[s[end]] > 1:
                    letter_hash[s[start]] -= 1
                    start += 1
                end+=1

            max_substring = max(max_substring, end-start)

        return max_substring