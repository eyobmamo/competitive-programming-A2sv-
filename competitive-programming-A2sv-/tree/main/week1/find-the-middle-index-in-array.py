class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ps=0
        total=sum(nums)
        for i in range(len(nums)):
            if ps ==total-nums[i]-ps:
                return i
            ps+=nums[i]    
        return -1        
            

        