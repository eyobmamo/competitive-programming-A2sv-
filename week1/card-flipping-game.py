class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        pair=[]
        identical=[]
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                identical.append(fronts[i])
            pair.append([fronts[i],backs[i]])
        pair2=pair.copy()
        pair.sort(key=lambda x:x[0])
        print(pair) 
        pair2.sort(key=lambda x:x[1])
        print(pair2)
        f=-1
        b=-1
        for i in range(len(fronts)):
            if  pair[i][0] not in identical:
                f=pair[i][0]
                break
        for i in range(len(fronts)):
            if pair2[i][1]not in identical:
                b=pair2[i][1]
                break
        if f !=-1 and b != -1:
            return(min(f,b))
        elif f==-1 and b != -1:
            return(b)
        elif f!=-1 and b ==-1:
            return(f)
        else:
            return(0)                    

                

        