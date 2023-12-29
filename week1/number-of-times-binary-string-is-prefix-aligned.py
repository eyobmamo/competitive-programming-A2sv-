class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        bin=[0]*(len(flips))
        count,trace=0,0
       
        for i,num in enumerate(flips):
            bin[num-1]=1
            if num-1<i  and bin[i]==1 and num-1 != i:
                trace += 2
                if trace == i+1:
                    count+=1
            elif num-1<i or bin[i]==1:
                trace += 1 
                if trace == i+1:
                    count+=1  
            print(trace ,i+1)                   
        return count        



          