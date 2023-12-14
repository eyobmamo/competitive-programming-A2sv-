class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner,loser,win,loss={},{},[],[]
        for match in matches:
            if match[0] in winner:
                winner[match[0]]+=1
            else:
                winner[match[0]]=1

        for match in matches:
            if match[1] in loser:
                loser[match[1]]+=1
            else:
                loser[match[1]]=1
        for key1,value1 in winner.items():
            if key1 not in loser:
                win.append(key1)
        for key2,value2 in loser.items():
            if value2 == 1:
                loss.append(key2)
        win.sort()
        loss.sort()        
        return [win,loss]                             
       
        