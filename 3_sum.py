class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        res_set = set()

        for i, num in enumerate(nums):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                added = num + nums[left] + nums[right]
                if added < 0:
                    left += 1
                elif added > 0:
                    right -= 1
                else:
                    num_set = [num, nums[left], nums[right]]
                    if tuple(num_set) in res_set:
                        left += 1
                    else:
                        result.append(num_set)
                        res_set.add(tuple(num_set))
                        left += 1
        return result