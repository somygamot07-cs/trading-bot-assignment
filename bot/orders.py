from client import client
from logging_config import logger

def place_market_order(symbol , side ,quantity):
    try:
        order = client.futures_create_order(
            symbol = symbol,
            side = side,
            type = "MARKET",
            quantity = quantity
            )
        logger.info(f"Market order success:{order}")
        return order
    except Exception as e:
        logger.error(f"Market Order Failed: {e}")
        raise

def place_limit_order(symbol , side , quantity , price):
    try:
        order = client.futures_create_order(
            symbol = symbol,
            side = side,
            type = "LIMIT",
            quantity = quantity,
            price = price,
            timeInForce = "GTC"
        )
        logger.info(f"linit order success:{order}")
        return order
    except Exception as e:
        logger.error(f"Limit Order Failed: {e}")
        raise