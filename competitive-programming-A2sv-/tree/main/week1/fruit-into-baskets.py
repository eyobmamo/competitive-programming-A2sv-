class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d={}
        l,cnt,rst=0,0,0
        for i in range(len(fruits)):
            d[fruits[i]]=d.get(fruits[i],0)+1
            cnt+=1
            while len(d)>2:
                d[fruits[l]]-=1
                cnt-=1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1
            rst=max(cnt,rst)
        return rst            


        