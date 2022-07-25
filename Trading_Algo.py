import webbrowser, requests, json, time

# This account contains no money or value, using the IDs would be a waste of your time

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
CLOCK_URL = "{}/v2/clock".format(BASE_URL)
WATCH_LIST_URL = "{}/v2/watchLists".format(BASE_URL)
STREAM_URL = "{}/stream".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': 'PK3YX3H7B0XCVQW2ZETN',
           'APCA-API-SECRET-KEY': 'JsuFWkkNXLkAnJfdjNf/i3ZfYjgpbYK4l/CziZn0'}

stock_amt = 0;

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

# Clock of market time
def get_clock():
    r = requests.get(CLOCK_URL, headers=HEADERS)
    return json.loads(r.content)

def get_watch_list():
    r = requests.get(WATCH_LIST_URL, headers=HEADERS)
    return json.loads(r.content)

def get_stream():
    da = {
        "action": "listening",
        "data": {
            "streams": ["trade_updates"]
        }
    }
    r = requests.get(STREAM_URL, json=da, headers=HEADERS)
    return json.loads(r.content)

# Shows the assets of the current account
def get_asset_url(symbol):
    ASSET_URL = "{}/v2/assets/".format(BASE_URL) + symbol
    r = requests.get(ASSET_URL, headers=HEADERS)
    return json.loads(r.content)

def get_position_url(symbol):
    POSITION_URL = "{}/v2/positions/".format(BASE_URL) + symbol
    r = requests.get(POSITION_URL, headers=HEADERS)
    return json.loads(r.content)

# Below represents how to buy/sell a stock ("PYPL"), how many (9), if your buying or selling ("buy"),
# where from ("market"), and what type of order ("gtc") or good-till-cancel
# create_order("PYPL", 9, "buy", "market", "gtc")

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side,
        "type": type,
        "time_in_force": time_in_force
    }
    r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
    return json.loads(r.content)

clock = get_clock()
IS_OPEN = clock.get("is_open")

# Prints "is_open" every 5 seconds while the market is open
while IS_OPEN:
    time.sleep(5)
    IS_OPEN = get_clock().get("is_open")
    print(IS_OPEN)

respose = IS_OPEN
print(respose)


#webbrowser.open('https://app.alpaca.markets/brokerage/stocks/SFET')
