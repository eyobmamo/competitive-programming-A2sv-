class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        average=0
        for x in range(1,len(salary)-1):
            average+=salary[x]
        return (average/(len(salary)-2))    


        