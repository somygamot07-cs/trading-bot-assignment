from client import client

try:
    account = client.futures_account()

    print("connected successfuly")
    print(account["totalWalletBalance"])

except Exception as e:
    print("Error " , e)
