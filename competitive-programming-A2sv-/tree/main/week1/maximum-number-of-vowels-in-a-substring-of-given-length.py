class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v="aeiou"
        count,left=0,0 
        for i in range(k):
            if s[i] in v:
                count+=1
        temp=count
        for i in range(k,len(s)):
            if s[i] in v:
                temp+=1
            if s[left] in v:
                temp-=1
            left+=1
            count=max(count,temp)
        return count            




        