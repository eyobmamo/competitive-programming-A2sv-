class Solution:
    def bestClosingTime(self, customers: str) -> int:
        privpen = customers.count("Y")
        curpen ,temp  = float(inf),float(inf)
        minhour = 0
       
        for i,s in enumerate(customers):
            if s == "Y":
                if curpen > privpen and temp > privpen :
                    minhour = i 
                curpen = privpen
                temp = min(privpen,temp)         
                privpen -= 1
                
                
            else:
                if curpen > privpen and temp > privpen :
                    minhour = i
                curpen = privpen
                temp = min(privpen,temp) 
                privpen +=1
                
        if curpen > privpen and temp > privpen:
            minhour = len(customers)     
        return minhour             
                
                



        