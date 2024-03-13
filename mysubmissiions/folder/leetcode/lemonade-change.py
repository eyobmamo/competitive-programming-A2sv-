class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        note5 ,note10 = 0,0
        for money in bills:
            if money == 5:
                note5 += 1    
            elif money == 10 and note5 >= 1:
                note5 -=1
                note10 += 1
            elif money == 10 and note5 < 1 :
                return False
            elif money == 20 and note5 >0 and note10 > 0:
                note5 -= 1 
                note10 -= 1 
            elif money == 20 and note5 >= 3 :
                note5 -=3
               
            elif money == 20 and note5 == 0 :
                return False
            elif money == 20 and note10 == 0 :
                return False    
        return True        




        