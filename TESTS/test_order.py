from orders import place_market_order

try:
    order = place_market_order(
        symbol="BTCUSDT",
        side = "BUY",
        quantity=0.001
    )

    print("order placed successfully")
    print("order ID :" , order["orderId"])
    print("status :",order["status"])
except Exception as e:
    print("Error:",e)

