class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls=[c.lower() for c in s if c.isalnum()]
        print(ls)
        if len(ls)>1:
            l,r=0,len(ls)-1
            while l < r:
                if ls[l] != ls[r]:
                    return False
                l+=1
                r-=1   
        
        return True        

        

        
        
        