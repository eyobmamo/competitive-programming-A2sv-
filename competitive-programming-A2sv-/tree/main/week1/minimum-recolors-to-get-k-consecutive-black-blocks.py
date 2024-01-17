class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt,left,res=0,0,float(inf)
        for i in range(k):
            if blocks[i] == "W":
                cnt+=1
        res=min(res,cnt)
        for i in range(k,len(blocks)):
            if blocks[left] =="W":
                cnt-=1
            
            if blocks[i] == "W":
                cnt+=1
            left+=1    
            res=min(res,cnt)
        return res            
            
            

                

        
        