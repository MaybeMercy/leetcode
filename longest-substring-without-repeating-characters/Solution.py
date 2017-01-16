# ecoding:utf-8

class Solution():
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
        	return 0
        longest_str = ''
        tmp_str = ''
        head = 0
        cursor = 0
        while cursor < len(s):
        	if s[cursor] not in tmp_str:
        		tmp_str += s[cursor]
        	else:
        		# 去重
        		while True:
        			head += 1
        			if head == cursor:
        				tmp_str = s[head]
        				break
        			tmp_str = s[head: cursor]
        			if s[cursor] not in tmp_str:
        				tmp_str += s[cursor]
        				break
        	if len(tmp_str) > len(longest_str):
        		longest_str = tmp_str
        	cursor += 1
        return longest_str
# Test
# s1 = "abcabcbb"
# s2 = 'bbbb'
# s3 = 'dvdf'
# solution = Solution()
# print solution.lengthOfLongestSubstring(s1)
# print solution.lengthOfLongestSubstring(s2)
# print solution.lengthOfLongestSubstring(s3)