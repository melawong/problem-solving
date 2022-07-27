# bucket sort 

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        for key, val in count.items():
            freq[val].append(key)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                if len(result) != k:
                    result.append(n)

        return result
