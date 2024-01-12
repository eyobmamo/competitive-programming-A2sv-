class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        d={}
        l,cnt=0,0
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
            if 0 in d:
                while d[0]>1:
                    d[nums[l]]-=1
                    l+=1
            cnt=max(cnt,i-l+1)
        return cnt-1    


        
        
        
        
        
        
        # left,cnt,z=0,0,0 
        # for i in range(len(nums)):
        #     if nums[left] == 0:
        #         left+=1
            
        #     if nums[i] == 0  and i>left:
        #         z+=1
        #         temp=i+1
        #     if z<2:
        #         cnt=max(cnt,i-left+1-z)
        #     else:
        #         left=temp
        #         z=0
        # if cnt == len(nums):
        #     return cnt-1
        # return cnt                       
                            


            
            
        