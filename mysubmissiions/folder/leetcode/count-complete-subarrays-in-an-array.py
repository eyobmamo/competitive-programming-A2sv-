class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distnict = len(set(nums))
        compsub = 0
        for i in range(len(nums)):
            temp =set()
            for j in range(i,len(nums)):
                temp.add(nums[j])
                if len(temp) == distnict :
                    compsub += 1
        return compsub            



        