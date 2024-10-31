import requests
import pandas as pd
import time

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

def fetch_btc_usdt_price():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f"API response: {data}")
        return float(data['price'])
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def monitor_price():
    prices = []
    while True:
        price = fetch_btc_usdt_price()
        if price is not None:
            print(f"Current BTC/USDT price: {price}")
            prices.append(price)
            with open("btc_usdt_results.txt", "a") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {price}\n")
        
        time.sleep(300)

        if len(prices) >= 10:
            df = pd.DataFrame(prices, columns=["Price"])
            df.to_csv("btc_usdt_results.csv", index=False, mode='a', header=not pd.io.common.file_exists("btc_usdt_results.csv"))
            prices.clear()

if __name__ == "__main__":
    print("BTC/USDT monitor started.")
    monitor_price()

