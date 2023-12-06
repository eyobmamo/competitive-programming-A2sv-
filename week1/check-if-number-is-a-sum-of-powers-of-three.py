class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        exponent_count=[]
        while n!=0:
            exp=0
            while n>=3**exp:
                exp+=1
            exponent_count.append(exp-1)
            n-=(3**(exp-1))
        if len(exponent_count)==len(set(exponent_count)):
            return True
        else:
            return False            

            


        