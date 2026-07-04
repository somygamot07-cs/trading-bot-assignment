from orders import place_limit_order

try:
    order = place_limit_order(
        symbol="BTCUSDT",
        side = "BUY", 
        quantity=0.001,
        price = 50000
    )
    print("Limit Order Place")
    print("order Id:",order["orderId"])
    print("Status:",order["status"])
except Exception as e:
    print("Error:" , e)