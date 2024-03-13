class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float(-inf)
        cursum =0
        for num in nums:
            if cursum < 0:
                cursum = 0
            cursum += num
            maxsum = max(cursum,maxsum)
        return maxsum        
        