class Solution:
    def minimumSteps(self, s: str) -> int:
        z_p,o_p = 0,0
        i,cnt,steps = len(s)-1,0,0
        while i >= 0:
            if s[i] == "0":
                cnt += 1
            else:
                steps += cnt
            i -= 1    
        return steps            


        
        
        