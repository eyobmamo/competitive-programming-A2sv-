class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d=Counter(s2[:len(s1)])
        
        ds1=Counter(s1)
        for i in range(len(s2)-(len(s1))+1):
            if d == ds1:
                return True
            else:
                d[s2[i]]-=1
                if d[s2[i]] == 0:
                    del d[s2[i]]
                if i+len(s1)<len(s2):    
                    d[s2[i+len(s1)]]=d.get(s2[i+len(s1)],0) + 1 
        return False           




        