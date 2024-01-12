class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        cnt,left=0,0
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
             
            while len(d) != (i+1)-left:
                d[s[left]] -=1
                if d[s[left]] == 0:
                    del d[s[left]]
                left+=1
            cnt=max(cnt,(i+1)-left)
        return cnt        
                



            

        
        