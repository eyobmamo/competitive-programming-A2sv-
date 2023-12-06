class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        index_zero=[-1]
        for i in range(len(nums)):
            if nums[i]==0:
                index_zero.append(i)
        index_zero.append(len(nums))
        count=0
        for i in range(1,len(index_zero)):
            count=max(index_zero[i]-index_zero[i-1]-1,count)
        return count    

             

                
        
        