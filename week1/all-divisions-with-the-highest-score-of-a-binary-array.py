class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        output=[]
        total=sum(nums)
        zeros=0
        dic_num={}
        for i in range(len(nums)):
            if nums[i]==0:
                output.append(total+zeros)
                zeros+=1
            else:
                output.append(total+zeros)
                total-=1
        output.append(zeros)
        maximum=max(output)
        i_max=[]
        for i,value in enumerate(output):
            if value==maximum:
                i_max.append(i)
        return i_max        




        
        