class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        f,s=0,0
        l1=len(nums1)
        l2=len(nums2)
        while  f<l1 and s<l2:
            if nums1[f]==nums2[s]:
                return nums1[f]
            elif nums1[f]<nums2[s]:
                f+=1
            else:
                s+=1
        return -1         
                        




        