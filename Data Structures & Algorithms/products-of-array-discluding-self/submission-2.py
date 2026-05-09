class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        
        for i in nums:
            if i==0:
                continue
            else:
                p*=i
        if nums.count(0)>1:
                nums=[0]*len(nums)
        elif nums.count(0)==1:
            n=nums.index(0)
            nums=[0]*len(nums)
            nums[n]=p
        else:
            for i in range(len(nums)):
                nums[i]=int(p/nums[i])
        return nums
                


                            
