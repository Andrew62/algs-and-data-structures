"""
https://leetcode.com/problems/online-stock-span/

Write a class StockSpanner which collects daily price quotes for some stock,
and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of
consecutive days (starting from today and going backwards) for which the
price of the stock was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85],
then the stock spans would be [1, 1, 1, 2, 1, 4, 6].



Example 1:

Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation:
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.

"""


class StockSpanner(object):

    def __init__(self):
        self.stock_prices = []

    def get_span(self, price: int) -> int:
        span = 0
        for val in self.stock_prices:
            if val <= price:
                span += 1
            else:
                break
        return span

    def next(self, price: int) -> int:
        """
        :type price: int
        :rtype: int
        """
        if not self.stock_prices:
            self.stock_prices.append(price)
            return 1

        self.stock_prices.insert(0, price)
        return self.get_span(price)


if __name__ == "__main__":
    stock_spanner = StockSpanner()
    stock_prices = [100, 80, 60, 70, 60, 75, 85]
    answers = [1, 1, 1, 2, 1, 4, 6]

    for idx, stock_price in enumerate(stock_prices):
        span = stock_spanner.next(stock_price)
        assert span == answers[idx], f"expected {answers[idx]} received {span}"
