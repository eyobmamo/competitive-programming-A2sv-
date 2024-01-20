class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        k=float("inf")
        l=0
        d={}
        for i in range(len(cards)):
            if cards[i] not in d:
                d[cards[i]]=i
            else:
                k=min(k,i-d[cards[i]]+1)
                d[cards[i]]=i
        if k != float("inf"):
            return k            
        else:
            return -1  

        