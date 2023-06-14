
def best_time_to_buy_and_sell_stock(stock_prices):
    # variables
    l, r, c_l, c_r = 0, 1, 0, 1
    maxP = 0

    # keep loop running till end of array
    while r < len(stock_prices):
        # check if is profitable to sell
        if stock_prices[l] < stock_prices[r]:
            profit = (stock_prices[r]-stock_prices[l])
            if maxP < profit:
                c_l, c_r = l, r
            maxP = max([maxP, profit])
        else:
            l = r
        r += 1
    return [c_l, c_r, maxP]


print(best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]))
