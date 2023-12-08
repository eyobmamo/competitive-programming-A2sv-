class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges_interval=set()
        for list1 in ranges:
            ranges_interval.update([num for num in range(list1[0],list1[1]+1)]) 
        sum_int={num for num in range(left,right+1)}
        return sum_int<=ranges_interval    
        