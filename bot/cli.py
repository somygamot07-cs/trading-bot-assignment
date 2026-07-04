import argparse
from orders import place_market_order,place_limit_order
from validators import(
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

parser = argparse.ArgumentParser()

parser.add_argument("--symbol" , required = True)
parser.add_argument("--side" , required = True)
parser.add_argument("--type" , required = True)
parser.add_argument("--quantity" , type = float , required = True)
parser.add_argument("--price" , type = float)

args = parser.parse_args()

if not validate_side(args.side):
    print("Invalid Side")
    exit()

if not validate_order_type(args.type):
    print("invalid Order Type")
    exit()

if not validate_quantity(args.quantity):
    print("Invalid Quantity")
    exit()

#market order

if args.type.upper() == "MARKET":

    order = place_market_order(
        args.symbol,
        args.side,
        args.quantity
    )

#limit order

elif args.type.upper() == "LIMIT":

    if args.price is None:
        print("Price required for LIMIT order")
        exit()
    
    if not validate_price(args.price):
        print("Invalid Price")
        exit()

    order = place_limit_order(
        args.symbol,
        args.side,
        args.quantity,
        args.price
    )

print("\nOrder Request Summary")
print("----------------------")
print("Symbol:", args.symbol)
print("Side:", args.side)
print("Type:", args.type)
print("Quantity:", args.quantity)

if args.type.upper() == "LIMIT":
    print("Price:", args.price)

print("\nOrder Response")
print("----------------")
print("Order ID:", order["orderId"])
print("Status:", order["status"])

if "executedQty" in order:
    print("Executed Qty:", order["executedQty"])