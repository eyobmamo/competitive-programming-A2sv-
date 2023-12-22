class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image)
        output=[]
        for r_n in range(n):
            output.append(image[r_n][::-1])
        print(output)    
        for r in range(n):
            output[r]=[0 if x==1 else 1 for x in output[r]]
        return output       
            
            
            

        