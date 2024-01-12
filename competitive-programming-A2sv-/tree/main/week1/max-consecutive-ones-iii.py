class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        z,cnt=0,0
        left=0
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
            while z>k:
                if nums[left]==0:
                    z-=1
                left+=1
            cnt=max(cnt,i-left+1)
        return cnt








        #     if nums[i]==0:
        #         z+=1
        #     cnt=max(cnt,i-left+1)
        #     while  z>k:
        #         flag=True
        #         if nums[left] == 0:
        #             z-=1
        #         left+=1

        # if flag==False and k==0:
        #     return cnt
        # else:    
        #     return cnt-1            


        