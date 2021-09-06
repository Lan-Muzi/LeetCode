class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # s = "PAYPALISHIRING"
        # iter 1 "P", row[0]
        #                 +1
        # iter 2 "A", row[1]
        #                 +1
        # iter 3 "Y", row[2]
        #                 -1
        # iter 4 "P", row[1]
        #                 -1
        # iter 5 "A", row[0]
        #                 +1
        # iter 6 "L", row[1]
        #                 +1
        # iter 7 "I", row[2]
        # ..........
        # row == 0 : step = 1
        # row == numRows - 1:step = -1
        # row += step        
        if numRows == 1 or numRows >= len(s):
            return s
        zigzag = ['' for x in range(numRows)]

        row, step = 0, 1

        for crct in s:
            zigzag[row] += crct

            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            
            row += step

        return ''.join(zigzag)
