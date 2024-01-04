class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i,coin=0,0
        while i<len(piles)/3:
            coin += piles[(len(piles)-2)-i*2]
            i+=1
        return coin    
        

        