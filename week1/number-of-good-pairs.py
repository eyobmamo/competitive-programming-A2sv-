class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pri=[]
        count_nums=[]
        for x in nums:
            if x not in pri:
                count_ele=nums.count(x)
                count_nums.append(count_ele)
                pri.append(x)
        num_good_pairs=0
        for x in count_nums:
            for y in range(x):
                num_good_pairs+=y
        return num_good_pairs                

        