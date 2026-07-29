class Solution:
    def addDigits(self, num: int) -> int:
        if num < 9:
            return num
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
        
        # while num>0:
        #     rem=num%10
        #     num=num//10
        #     sum=sum+rem
        # return sum
    
