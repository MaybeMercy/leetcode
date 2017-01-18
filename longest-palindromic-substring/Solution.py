class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 2:
            return s
        mx = ''
        # for odd
        for i in range(len(s)):
            tmps = s[i]
            for j in range(1, len(s) / 2 + 1):
                if (i - j) >= 0 and (i + j) < len(s):
                    if s[i-j] == s[i+j]:
                        tmps = s[i-j] + tmps + s[i+j]
                    else:
                        break
                else:
                    break
            # print 'tmps ', tmps
            if len(tmps) > len(mx):
                mx = tmps
        # print mx
        # for even
        for i in range(len(s)):
            if i+1 == len(s):
                break
            else:
                if s[i] == s[i+1]:
                    tmps = s[i] + s[i+1]
                else:
                    continue
            for j in range(1, len(s) / 2 + 1):
                if i - j >= 0 and i + 1 + j < len(s):
                    if s[i-j] == s[i+1+j]:
                        tmps = s[i-j] + tmps + s[i+1+j]
                    else:
                        break
                else:
                    break
            if len(tmps) > len(mx):
                mx = tmps

        return mx

# Test
solution = Solution()
print solution.longestPalindrome('ccccc')