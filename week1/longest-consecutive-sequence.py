class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=1
        if not nums:
            return 0
        else:

            for num in num_set:
                if num-1 not in num_set:
                    length=1
                    while num+1 in num_set:
                        num+=1
                        length+=1
                    longest=max(length,longest)
        return longest            

                   




        