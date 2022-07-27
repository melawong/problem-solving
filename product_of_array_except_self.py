class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        prefix = 1
        postfix = 1

        for num in nums:
            result.append(prefix)
            prefix *= num

        for i in range(len(nums) -1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result