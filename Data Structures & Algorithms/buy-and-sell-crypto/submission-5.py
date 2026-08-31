class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=0
        w=0
        for i in range(1,len(prices)):
            if prices[i]>=prices[w]:
                if (prices[i]-prices[w])>max:
                    max=prices[i]-prices[w]
            elif prices[i]<prices[w]:
                w=i
        return max