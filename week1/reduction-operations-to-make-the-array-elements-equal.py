class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        l=len(nums)
        count=0
        set1=set(nums)
        l1=list(set1)
        l1.sort()
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1    
        for i,v in enumerate(l1):
            count+=d[v]*i
        return count    
                
            
        
        
        

            



            


    

            
        
        