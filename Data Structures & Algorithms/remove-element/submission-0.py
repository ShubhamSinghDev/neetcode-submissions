class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=nums.count(val)
        for i in range(l):
            nums.remove(val)
        return len(nums)