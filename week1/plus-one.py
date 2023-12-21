class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1]+=1
            return digits
        else:
            number="".join(str(x) for x in digits)
            print(number)
            number=int(number)+1
            return [int(x) for x in str(number)]
            #number+=1
            return [num for num in str(number)]

        