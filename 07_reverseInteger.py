class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        # return the obsolute value of a number
        a = abs(x)
        while(a != 0):
            temp = a % 10
            #print('a', a)
            num = num * 10 + temp 
            #print('num', num)
            a = int(a/10)
        
        if x > 0 and num < 2147483647:
            return num
        elif x < 0 and num <= 2147483647:
            return -num
        else:
            return 0
