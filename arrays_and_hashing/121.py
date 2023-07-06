def maxProfit(prices):
    profit = 0
    for index, i in enumerate(prices):
        for j in (index + 1, len(prices)):
            if profit > j - i:
                    profit = i - j
    print(profit)

maxProfit([7,1,5,3,6,4])
