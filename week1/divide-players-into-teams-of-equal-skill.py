class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0]*skill[1]
        elif len(skill)>2:
            skill.sort()
            l,r=1,len(skill)-2
            while l<r:
                if skill[l]+skill[r]!=skill[l-1]+skill[r+1]:
                    return -1
                l+=1
                r-=1
            l,r=0,len(skill)-1
            sums=0    
            while l<r:    
              sums+=(skill[l]*skill[r])
              l+=1
              r-=1 
        return sums             
        