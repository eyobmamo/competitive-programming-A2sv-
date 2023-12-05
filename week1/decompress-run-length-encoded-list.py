class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output=[]
        for x in range(len(nums)):
            if x%2==0:
                for y in range(nums[x]):
                    output.append(nums[x+1])
        return output            
        