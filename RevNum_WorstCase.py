class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x=abs(x)
        revNum=0
        while(x>0):
            r=x%10
            x=x//10
            revNum=(revNum*10)+r
        revNum*=sign
        if revNum>2**31-1 or revNum<-2**31:
            return 0 
        return revNum
