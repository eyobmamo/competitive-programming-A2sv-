class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output=[]
        arr=[]
        for num in arr2:
            output.extend([num]*arr1.count(num))
        for num in arr1:
            if num not in arr2:
                arr.append(num)
        arr.sort()        
        output.extend(arr)        
                    
        return output    

        
        