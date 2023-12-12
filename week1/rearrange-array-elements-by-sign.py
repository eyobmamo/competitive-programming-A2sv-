class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l_neg,l_pos=[],[]
        rearrange=[]
        for i,num in enumerate(nums):
            if num<0:
                l_neg.append(num)
            else:
                l_pos.append(num)
        for i in range(len(l_neg)):
            rearrange.append(l_pos[i])
            rearrange.append(l_neg[i])
        return rearrange              

             
        