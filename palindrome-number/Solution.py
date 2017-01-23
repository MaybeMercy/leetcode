class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        s = str(x)
        for i in range(len(s)):
            print i, len(s)-1-i
            if i > len(s)-1-i:
                break
            if s[i] != s[len(s)-1-i]:
                return False
        return True

solution = Solution()
print solution.isPalindrome(121)
