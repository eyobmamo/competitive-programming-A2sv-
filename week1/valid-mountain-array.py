class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)>=3 and arr[0]<arr[1]:

            change=0
            for i in range(len(arr)-1):
                if arr[i]>=arr[i+1]:
                    change=i
                    break
            for i in range(change,len(arr)-1):
                if arr[i]<=arr[i+1]:
                    return False
            return True
        else:
            return False            


                

        