class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        output=[]
        out=[]
        for i in range(len(s)):
            out.append(ord(s[i]))
        temp=[0]*len(s)
        for i in range(len(shifts)):
            if shifts[i][2]==0:
                temp[shifts[i][0]]+=-1
                if shifts[i][1]+1<len(temp):
                    temp[shifts[i][1]+1]+=1
            if  shifts[i][2]==1 :
                temp[shifts[i][0]]+=1
                if shifts[i][1]+1<len(temp):
                   temp[shifts[i][1]+1]+=-1
        maxi=0            
        for  i in range(len(temp)):
            maxi+=temp[i]
            output.append(maxi)
        print(output)
        out=[num-97 for num in out]
        for i in range(len(out)):
            out[i]=(out[i]+output[i])%26
            out[i]=chr(out[i]+97)
             

         
        return "".join( out)

        
            
        


                      
            


        