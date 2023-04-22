def getDataPoint(quote):
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price)/2
    return stock, bid_price, ask_price, price
def getRatio(price_a, price_b):
    if(price_b == 0):
        return
    return price_a/price_b
if __name__ == "__main__":
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random())).read())
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %S at (bid:%S, ask:%S, price:%S))" % (stock, bid_price, ask_price, price))

        price("Ratio %S" % getRatio(price["ABC"], prices["DEF"]))
