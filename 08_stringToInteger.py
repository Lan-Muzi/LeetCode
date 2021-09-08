class Solution:
    def myAtoi(self, s: str) -> int:
        stripStep = str.strip(s)

        if stripStep == "" or stripStep == "-" or stripStep == "+":
            return 0

        s1 = re.match('[^\d]+', (stripStep.lstrip("-")).lstrip("+"))

        if s1 != None:
            return 0
        else:
            s1 = re.search('\-*\+*\d+', stripStep).group()

        if s1[0:2] == "--" or s1[0:2] == '-+' or s1[0:2] == '++':
            return 0

        result = int(s1)
        if result > 0:
            return 2147483647 if result > 2147483647 else result
        else:
            return -2147483648 if result < -2147483648 else result
