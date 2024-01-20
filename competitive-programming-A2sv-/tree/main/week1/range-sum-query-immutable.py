class NumArray:

    def __init__(self, nums: List[int]):
        self.prif=[0]*(len(nums)+1)
        for i in range(len(nums)):
            self.prif[i+1]=self.prif[i]+nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prif[right+1]-self.prif[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)