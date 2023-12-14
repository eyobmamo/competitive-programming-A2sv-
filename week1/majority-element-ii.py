class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        true_shold=len(nums)//3
        num_dic={}
        appear=[]
        for num in nums:
            if num in num_dic:
                num_dic[num] +=1
            else:
                num_dic[num]=1
        for num in num_dic:        
            if num_dic[num]>true_shold:
                appear.append(num)        
        return appear                
       

   


        
        