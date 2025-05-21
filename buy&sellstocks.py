prices=[7,4,1,3]
buy_stock=min(prices)
buy_index=prices.index(buy_stock)
max_profit=0

for price in prices:
    if price > buy_stock:
        max_profit=price-buy_stock
    
print(max_profit)
 
    
    
    