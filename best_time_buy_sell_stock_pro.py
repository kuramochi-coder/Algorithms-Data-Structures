
def buy_and_sell(arr):
    max_profit = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            max_profit = max(max_profit, arr[j] - arr[i])
    return max_profit


print(buy_and_sell([9, 11, 8, 5, 7, 10]))


def buy_and_sell2(arr):
    max_current_price = 0
    max_profit = 0

    for price in arr[::-1]:
        max_current_price = max(max_current_price, price)
        max_profit = max(max_profit, max_current_price - price)

    return max_profit


print(buy_and_sell2([9, 11, 8, 5, 7, 10]))