class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {")":"(", "]":"[", "}":"{"}
        strChars = []

        if len(s) < 2:
            return False

        for char in s:
            if char in hashMap.keys():
                if len(strChars) == 0:
                    return False
                elif strChars[-1] != hashMap[char]:
                    return False
                strChars.pop()
            else:
                strChars.append(char)

        if not len(strChars) == 0:
            return False

        return True