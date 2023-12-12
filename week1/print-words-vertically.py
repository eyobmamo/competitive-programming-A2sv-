class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=list(s.split())

        max_len=0
        for ele in s:
            max_len=max(max_len,len(ele))

        for i in range(len(s)):
            if len(s[i])<max_len:
                s[i]=s[i]+" "*(max_len-len(s[i]))

        grid=[list(ele) for ele in s]

        result=[]
        for i in range(max_len):
            temp_str=""
            for j in range(len(grid)):
                temp_str+=grid[j][i]
            
            # removing the spaces that comes in last
            temp_str=temp_str.rstrip() 
            result.append(temp_str)
        
        return result