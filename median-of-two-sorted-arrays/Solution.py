class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = []
        if len(nums1) == 0:
            num = nums2[:]
        if len(nums2) == 0:
            num = nums1[:]
        c1 = 0
        c2 = 0
        while c1 < len(nums1) and c2 < len(nums2):
        	if nums1[c1] < nums2[c2]:
        		num.append(nums1[c1])
        		c1 += 1
        	else :
        		num.append(nums2[c2])
        		c2 += 1
        	if c1 == len(nums1):
        		num.extend(nums2[c2:])
        		break
        	if c2 == len(nums2):
        		num.extend(nums1[c1:])
        		break
        if len(num) % 2 == 0:
        	return (num[len(num) / 2] + num[len(num) / 2 - 1]) * 0.5
        else:
        	return num[(len(num) -1) / 2]

# Test
# solution = Solution()
# s1 = [1, 3]
# s2 = [2]
# s3 = [] # 这样的情况需要注意
# print solution.findMedianSortedArrays(s1, s2)
