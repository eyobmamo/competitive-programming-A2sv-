class Solution:
    def sortSentence(self, s: str) -> str:
        strs=s.split()
        d={}
        for string in strs:
            d[int(string[-1])]=string[:len(string)-1]
        arr=['']*len(strs)    
        for k,v in d.items():
            arr[k-1]=v
        return " ".join(arr)    


        