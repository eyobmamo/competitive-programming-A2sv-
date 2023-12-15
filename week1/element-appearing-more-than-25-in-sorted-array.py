class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        qua_num=len(arr)//4
        for num in arr:
            if arr.count(num)>qua_num:
                return num
        return None        
            
        
      




        