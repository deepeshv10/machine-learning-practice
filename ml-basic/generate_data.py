"""One-time script to generate stock_trades.csv"""
import numpy as np
import pandas as pd
np.random.seed(42)
n = 1000
symbols = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]
sector_map = {
    "AAPL": "Technology",
    "GOOG": "Technology",
    "MSFT": "Technology",
    "AMZN": "E-Commerce",
    "TSLA": "Automotive",
}
mcap_map = {"AAPL": 2800, "GOOG": 1900, "MSFT": 2700, "AMZN": 1600, "TSLA": 800}
base_price_map = {"AAPL": 175, "GOOG": 140, "MSFT": 380, "AMZN": 180, "TSLA": 250}
symbol = np.random.choice(symbols, n)
sector = np.array([sector_map[s] for s in symbol])
market_cap = np.array([mcap_map[s] + np.random.normal(0, 50) for s in symbol]).round(1)
buy_price = np.array(
    [base_price_map[s] * np.random.uniform(0.85, 1.15) for s in symbol]
).round(2)
volume = np.random.randint(100, 50000, n)
holding_days = np.random.randint(1, 120, n)
pe_ratio = np.random.uniform(10, 60, n).round(2)
daily_volatility = np.random.uniform(0.5, 5.0, n).round(3)
moving_avg_50 = (buy_price * np.random.uniform(0.95, 1.05, n)).round(2)
rsi = np.random.uniform(15, 85, n).round(2)
price_change = buy_price * np.random.normal(0.02, 0.08, n)
sell_price = (buy_price + price_change).round(2)
profitable = (sell_price > buy_price).astype(int)
df = pd.DataFrame(
    {
        "trade_id": range(1, n + 1),
        "symbol": symbol,
        "sector": sector,
        "buy_price": buy_price,
        "sell_price": sell_price,
        "volume": volume,
        "holding_days": holding_days,
        "market_cap_billion": market_cap,
        "pe_ratio": pe_ratio,
        "daily_volatility": daily_volatility,
        "moving_avg_50": moving_avg_50,
        "rsi": rsi,
        "profitable": profitable,
    }
)
df.to_csv("c:/Dev/gcp/machine-learning/data/stock_trades.csv", index=False)
print(f"Created {len(df)} rows")
print(f"Class balance: {df['profitable'].value_counts().to_dict()}")
print(df.head())