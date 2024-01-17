class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float('inf')
        left,temp=0,0
        for i in range(len(nums)):
            temp+=nums[i]

            while temp >= target :
                mini=min(mini,i-left+1)
                temp-=nums[left]
                left+=1
        if  mini ==float("inf"):
            return 0
        else:
            return mini            


        