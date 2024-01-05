class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p=0
        for s in range(len(nums)):
            if nums[p] == 0 and nums[s] !=0:
                nums[p],nums[s]=nums[s],nums[p]
            if nums[p] != 0:
                p+=1    
       



        





        """
        Do not return anything, modify nums in-place instead.
        """
        