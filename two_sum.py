class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        currInx = 0

        for num in nums:
            if target - num not in hashMap:
                hashMap[num] = currInx
                currInx += 1
            else:
                return [currInx, hashMap[target-num]]