class Solution:
    def totalMoney(self, n: int) -> int:
        balance=0
        no_week=n//7
        remainder=n%7
        common=0
        for i in range(no_week):
            common+=i*7
        if n<7:
            balance+=((remainder+1)*(remainder))/2
        else:
            balance+=(28*no_week+common+((no_week+1)*remainder)+((remainder*(remainder-1)/2)))
        return int(balance)

        