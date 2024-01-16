class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rs=[]
        sumi=0
        for i in range(len(nums)):
            sumi+=nums[i]
            rs.append(sumi)
        return rs    
