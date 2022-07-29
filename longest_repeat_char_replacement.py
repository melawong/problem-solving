class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_ltrs = {}
        result = 0
        l = 0
        maxfrq = 0

        for r in range(len(s)):
            if s[r] not in hash_ltrs:
                hash_ltrs[s[r]] = 1
            else:
                hash_ltrs[s[r]] += 1

            maxfrq = max(maxfrq, hash_ltrs[s[r]])

            while (r - l + 1) - maxfrq > k:
                hash_ltrs[s[l]] -= 1
                l += 1

            result = max(result, (r - l + 1))

        return result