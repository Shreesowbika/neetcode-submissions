class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        s=0
        m=0
        for i in range(len(gain)):
            s+=gain[i]
            m=max(m,s)
        return m
