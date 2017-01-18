# coding=utf-8
# 本道题题意不是很清晰，有些边界条件比较蛋疼，"+-2" 应该返回0，"   - 321" 也应该返回0
class Solution(object):
    def myAtoi(self, str):
        """
        :param str:
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        sign = 1
        i = 0
        if str == '':
            return 0
        while i < len(str) and str[i].isspace():
            i += 1
        if i < len(str) and str[i] == '-':
            sign = -1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            i += 1
        j = i
        while j < len(str) and str[j].isdigit():
            j += 1
        ss = str[i:j]
        if not ss.isdigit():
            return 0
        result = int(str[i:j]) * sign
        if result < INT_MIN:
            result = INT_MIN
        if result > INT_MAX:
            result = INT_MAX
        return result

# Test
solution = Solution()
print solution.myAtoi("   - 321")

