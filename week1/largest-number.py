class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums.count(0)==len(nums):
            return "0"
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if int(str(nums[j])+str(nums[j+1]))>int(str(nums[j+1])+str(nums[j])):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        nums.reverse()
        
        return "".join(str(num) for num in nums)            
                
        
        