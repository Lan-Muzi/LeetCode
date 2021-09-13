class Solution:
    def intToRoman(self, num)
        # values = [1000, 900, 500, 400,....]
        # numerals= ['M', 'CM', 'D','CD',...]
        # input:1994
        # 1994 > ? 1000 => M
        # 994 > ? 900 =>MCM
        # ...........
        # 94 >? 90 => MCMXC
        # ............
        # 4 >? 4 => MCMXCIV
        values =[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        numerals = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']

        result = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                result += numerals[i]

        return resul
