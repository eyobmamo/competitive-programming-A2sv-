class Solution:
    def longestPalindrome(self, s: str) -> int:
        d1 = dict()
        for char in s:
            if char not in d1:
                d1[char] = 1
            else:
                d1[char] += 1
        cnt = 0   
        temp = 0     

        for key,val in d1.items():
            if val % 2 == 0:
                cnt += val
            else:
                cnt += val-1
                temp =max(temp,val)
        if temp != 0:
            return cnt+1        
        else:        
            return cnt        


        