class Solution:
    def romanToInt(self, s: str) -> int:
        roma={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        num=[]
        for x in range(len(s)):
            num.append(roma[s[x]])        
        sum=0
        x=0
        while x<=len(num)-1:
            if x==len(num)-1:
                sum+=num[x]
                x+=1
            elif num[x]>=num[x+1] :
                sum+=num[x]
                x+=1    
            elif num[x]<num[x+1]:
                sum+=num[x+1]-num[x]
                x+=2
            elif x==len(num)-1:
                sum+=num[x]
                x+=1 
            else:
                pass       
        return sum 
        


        