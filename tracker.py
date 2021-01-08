from iexfinance.stocks import Stock
from scraper import popularTickers

IEX_TOKEN = "pk_6c5be8a9f6cc41239fae7f0975da888f"

def closePrice(ticker):
    a = Stock(ticker, token = IEX_TOKEN)
    previousClose = a.get_quote()['previousClose']
    currentClose = a.get_quote()['iexClose']
    return previousClose, currentClose
    
x, y = popularTickers()
# how much top tickers you want
x = x[:10]
y = y[:10]
print(x)
print(y)

amount = 10000
finalAmount = 0
total = sum(y)
for i in range(len(y)):
    previous, current = closePrice(x[i])
    result = ((current - previous) / previous + 1) * (y[i] / total) * amount
    print(result)
    finalAmount += result
print(finalAmount)
percentChange = ((finalAmount - amount) / amount * 100)
print(percentChange)