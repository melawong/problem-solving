class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        word_list = []
        curr_word = ""

        for char in s:
            if char != " ":
                curr_word+=(char)
            else:
                if len(curr_word) != 0:
                    word_list.append(curr_word)
                    curr_word = ""

        if len(curr_word) != 0:
            word_list.append(curr_word)

        return len(word_list[len(word_list)-1])   