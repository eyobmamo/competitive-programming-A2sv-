class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_y=[]
        for x in range(n):
            x_y.append(nums[x])
            x_y.append(nums[x+n])
        return x_y    
        