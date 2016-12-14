class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0

        lowest = prices[0]
        highest = prices[0]
        diff = 0
        length = len(prices)

        for i in range (0, length):
            current = prices[i]
            if current < lowest:
                lowest = current
                highest = 0

            if current > highest:
                highest = current

            new_diff = highest - lowest
            if new_diff > diff:
                diff = new_diff

        return diff


s = Solution()

print(s.maxProfit([7, 2, 11, 1, 5, 3, 6, 4]))