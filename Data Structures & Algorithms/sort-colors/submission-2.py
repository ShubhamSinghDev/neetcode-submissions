class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        lst=[0,0,0]
        for i in nums:
            if i==0:
                lst[0]+=1
            if i==1:
                lst[1]+=1
            if i==2:
                lst[2]+=1
        for i in range(lst[0]):
                nums[i]=0
        for k in range(lst[1]):
            nums[lst[0]+k]=1
        for l in range(lst[2]):
            nums[lst[0]+lst[1]+l]=2 