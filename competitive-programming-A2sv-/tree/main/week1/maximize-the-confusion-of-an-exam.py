class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        cnt,maxi,left=0,0,0
        for i in range(len(answerKey)):
            if answerKey[i] == "F":
                cnt+=1
            while cnt>k:
                if answerKey[left] == "F":
                    cnt-=1
                left+=1
            maxi=max(maxi,i-left+1)
            print("f to t",maxi)

        cnt,left=0,0
        for i in range(len(answerKey)):
            if answerKey[i] == "T":
                cnt+=1
            while cnt>k:
                if answerKey[left] == "T":
                    cnt-=1
                left+=1
            maxi=max(maxi,i-left+1)
            print("T to f",maxi)
        return maxi            




        