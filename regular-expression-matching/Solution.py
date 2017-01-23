# coding=utf-8

class Solution(object):
    # 使用递归的解法
    # 如果P[j + 1] != '*'，S[i] == P[j] = > 匹配下一位(i + 1, j + 1)，S[i] != P[j] = > 匹配失败；
    # 如果P[j + 1] == '*'，S[i] == P[j] = > 匹配下一位(i + 1, j + 2)
    # 或者(i, j + 2)，S[i] != P[j] = > 匹配下一位(i, j + 2)。
    # 匹配成功的条件为S[i] == '\0' && P[j] == '\0'。
    def isMatch(self, s, p):
        if len(p) == 0:
            return len(s) == 0
        if len(p) == 1 or p[1] != '*':
            if len(s) == 0 or (s[0] != p[0] and p[0] != '.'):
                return False
            return self.isMatch(s[1:], p[1:])
        else:
            i = -1
            length = len(s)
            while i < length and (i < 0 or p[0] == '.' or p[0] == s[i]):
                if self.isMatch(s[i+1:], p[2:]):
                    return True
                i += 1
            return False
