class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic_com={}
        common_s=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                   dic_com[list1[i]] = i+j
        for key,value in dic_com.items():
            if value == min(dic_com.values()):
                common_s.append(key)
        return common_s                                       

       
       
        