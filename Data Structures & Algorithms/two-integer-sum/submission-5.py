class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i in nums:
            p=target-i
            if p in nums[nums.index(i)+1:]:
                return [nums.index(i),nums[nums.index(i)+1:].index(p)+nums.index(i)+1]    