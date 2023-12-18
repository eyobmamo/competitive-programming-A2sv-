class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even,odd = 0,0
        for num in nums:
            if num%2==1:
                odd+=num
            else:
                even+=num
				
        ans = []
        for query in queries:
            val,idx = query
            preval = nums[idx]
            if preval%2 == 0:
                even -= preval
            nums[idx] = nums[idx] + val
            if nums[idx]%2==0:
                even += nums[idx]
            ans.append(even)
        return ans

        