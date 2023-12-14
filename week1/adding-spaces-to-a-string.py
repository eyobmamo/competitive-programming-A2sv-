class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        mod_s=""
        ind=0
        for i in range(len(s)):
            if len(spaces)>ind and i == spaces[ind]:
                mod_s+=" "
                mod_s+=s[i]
                ind+=1
            else:
                mod_s+=s[i]    
        return mod_s
        