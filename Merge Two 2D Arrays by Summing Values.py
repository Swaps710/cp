from collections import defaultdict
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        d1, d2 = defaultdict(int,{a:b for a,b in nums1}),defaultdict(int,{a:b for a,b in nums2})
        return [[k, d1[k] + d2[k]] for k in sorted(set(d1.keys()).union(set(d2.keys())))]
        
