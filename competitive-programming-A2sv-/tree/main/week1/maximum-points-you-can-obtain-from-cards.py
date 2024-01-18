class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxi=sum(cardPoints[:k])
        result=0
        result=max(result,maxi)
        l=k-1
        for i in range(-1,-(k+1),-1):
            print(i)
            maxi-=cardPoints[l]
            maxi+=cardPoints[i]
            l-=1
            result=max(result,maxi)
        return result    

            


        