class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, big_diff = prices[0] , 0

        for elem in prices:
            if elem < lowest:
                lowest = elem
            if elem - lowest > big_diff:
                big_diff = elem - lowest

        return big_diff