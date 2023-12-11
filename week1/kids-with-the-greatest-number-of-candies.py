class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        maximum_c=max(candies)
        for candie in candies:
            if candie + extraCandies >= maximum_c:
                result.append(True)
            else:
                result.append(False)    
        return result        

        