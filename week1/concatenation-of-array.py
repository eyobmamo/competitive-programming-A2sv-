class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copy_nums=nums.copy()
        nums.extend(copy_nums)
        return nums
        