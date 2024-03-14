class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d1 = dict()
        for answer in answers:
            if answer not in d1:
                d1[answer] = 1
            else:
                d1[answer] +=1 
        minrab =0
        r,q = 0,0
        for key, val  in d1.items():
            r = (val// (key+1)) * (key+1)
            q = 0
            if val % (key + 1)>0:
                q = (key + 1)
            minrab += r+q
        return minrab    
            


        print(d1)