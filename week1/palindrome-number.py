class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            y=str(x)
            z=y[::-1]
            return int(z)==x
        else:
            return False    
        