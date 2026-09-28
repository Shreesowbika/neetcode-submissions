class Solution(object):
    def intersection(self, nums1, nums2):
        c=set(nums1+nums2)
        out=[]
        for i in c:
            if i in nums1 and i in nums2:
                out.append(i)
        return out
        