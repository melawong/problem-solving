class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_hashes = {}
        result = []

        for word in strs:
            curr_hash = {}
            for char in word:
                if char in curr_hash:
                    curr_hash[char] += 1
                else:
                    curr_hash[char] = 1

            group_index = self.get_key(word_hashes, curr_hash)

            if group_index == None:
                word_hashes[len(result)] = curr_hash
                result.append([word])
            else:
                result[group_index].append(word)
        return result

    def get_key(self, word_hashes, curr_hash):
        for index in word_hashes:
            if word_hashes[index] == curr_hash:
                return index
        return None