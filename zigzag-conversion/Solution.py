# coding:utf-8
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        step = 2 * numRows - 2
        ss = ''
        for i in range(numRows):
            j = i
            c = 1
            while j < len(s):
                ss += s[j]
                # 当 i 不是 0 位和 n-1 位时，有2个值
                if i != 0 and i != numRows - 1:
                    if c * step - i < len(s):
                        ss += s[c * step - i]
                c += 1
                j += step
        print 's ', ss
        # return ss

# Test
solution = Solution()
solution.convert("PAYPALISHIRING", 3)
