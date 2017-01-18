# coding=utf-8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        neg = 1
        if x < 0:
            neg, x = -1, -x
        while x > 0:
            last_digit = x % 10
            result = result * 10 + last_digit
            x /= 10
        result *= neg
        # 如果使用 sys.maxint 可能会导致不准，32位的不通过
        if result < -(1 << 31) or result > (1 << 31) - 1:
            result = 0
        return result

