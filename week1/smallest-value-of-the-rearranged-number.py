class Solution:
    def smallestNumber(self, num: int) -> int:
        if num<0:
            num=str(num)
            num_s=num[1:]
            num_l=[int(n) for n in num_s]
            num_l.sort(reverse=True)
            return int("".join(str(n) for n in num_l))*-1
        else:
            num_l=[int(n) for n in str(num)]
            num_l.sort()
            print(num_l)
            if num_l[0]==0:
                for i,n in enumerate(num_l):
                    if n != 0:
                        num_l[0],num_l[i]=num_l[i],num_l[0]
                        break
            return int("".join(str(n) for n in num_l))            
                        

                

        