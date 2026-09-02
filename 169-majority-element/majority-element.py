class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        d={}
        for num in nums:
            d[num] = d.get(num, 0) + 1

        return max(d, key=d.get)