class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums)>=k:
            l=len(nums)-(k-1)
            sumi=(sum(nums[:k]))
            s,end=0,k
            c,maxi=0,sumi/k
            while end<len(nums):
                sumi+=nums[end]
                sumi-=nums[s]
                maxi=max(maxi,(sumi)/k)
                end+=1
                s+=1
        return maxi    





        
        