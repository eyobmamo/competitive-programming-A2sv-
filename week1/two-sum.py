class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dic={}
        for ind,val in enumerate(nums):
            diff=target-val

            if diff in num_dic:
                return [num_dic[diff],ind]

            num_dic[val]=ind
        return []    

        