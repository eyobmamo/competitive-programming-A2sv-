class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        s1=set(nums1)
        s2=set(nums2)
        s3=s1&s2
        for num in s3:
            output.extend([num]*min(nums1.count(num),nums2.count(num)))
        return output    
       
        
        
    
        
    

        