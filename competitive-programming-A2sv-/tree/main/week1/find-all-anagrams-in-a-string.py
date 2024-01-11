class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target=Counter(p)
        cur=Counter(s[0:len(p)])
        output=[]
        iter=0
        if target == cur:
            output.append(iter)
        
        while iter <len(s)-(len(p)):
            cur[s[iter]]-=1
            if cur[s[iter]]==0:
                del cur[s[iter]]
            cur[s[iter+len(p)]]=cur.get(s[iter+len(p)],0)+1
            if target ==cur:
                output.append(iter+1)
            iter+=1
        return output        

            



        

        