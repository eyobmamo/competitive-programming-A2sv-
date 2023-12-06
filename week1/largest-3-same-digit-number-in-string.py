class Solution:
    def largestGoodInteger(self, num: str) -> str:
        store_int=[]
        for x in range(10):
            if  str(x)*3 in num:
                store_int.append(x)
        if len(store_int)>0:
            return str(store_int[len(store_int)-1])*3
        else:
            return ""            
        