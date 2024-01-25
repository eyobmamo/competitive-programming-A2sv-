class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result=[]
        flen,slen=len(firstList),len(secondList)
        fpt,spt=0,0
        while fpt<flen and spt<slen:
            if firstList[fpt][0] <= secondList[spt][1] and firstList[fpt][1]>=secondList[spt][0]:
                result.append([max(firstList[fpt][0],secondList[spt][0]),min(firstList[fpt][1],secondList[spt][1])])

            elif firstList[fpt][1] >= secondList[spt][0] and firstList[fpt][0]<=secondList[spt][1]:
                result.append([max(firstList[fpt][0],secondList[spt][0]),min(firstList[fpt][1],secondList[spt][1])])

            elif firstList[fpt][1] < secondList[spt][0]:
                pass

            elif firstList[fpt][0] < secondList[spt][1]:
                pass
            if firstList[fpt][1] < secondList[spt][1]:
                fpt+=1
            else:
                spt+=1
        return result                             

        