class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ice_p,count=0,0
        for i in range(len(costs)):
            if ice_p+costs[i]<=coins:
                ice_p+=costs[i]
                count+=1
            else:
                break    
        return count        

        