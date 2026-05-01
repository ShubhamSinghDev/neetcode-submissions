class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            s=list(set(nums))
            c=0
            for i in s:
                if nums.count(i)>c:
                    c=nums.count(i)
                    n=i
            return n
