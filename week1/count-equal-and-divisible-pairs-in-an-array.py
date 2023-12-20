class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            for n in range(len(nums)):
                if n != i and nums[n]==nums[i] and (i*n)%k==0:
                    count +=1
        return int(count/2)            


        