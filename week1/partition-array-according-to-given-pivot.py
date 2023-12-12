class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_p,equal_p,greater_p=[],[],[]
        for num in nums:
            if pivot>num:
                less_p.append(num)
            elif pivot==num:
                equal_p.append(num)
            else:
                greater_p.append(num)
        return less_p+equal_p+greater_p        
                        
        