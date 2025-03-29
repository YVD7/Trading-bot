# Live trading bot dash board
import datetime, time
import yfinance as yf
import pandas as pd
from rich import print as rprint
from rich.live import Live
from rich.table import Table

# import talib as ta


"""Make a Table"""

table = Table()
table.add_column("DateTime")
table.add_column("Ticker")
table.add_column("Price")

with Live(table, refresh_per_second=60) as live:
    while True:
        btcusd = yf.download(tickers="BTC-USD", interval="1m", auto_adjust=True)
        data = pd.DataFrame({
            "Date": btcusd.index,
            "Open": btcusd.Open.values.flatten(),
            "High": btcusd.High.values.flatten(),
            "Low": btcusd.Low.values.flatten(),
            "Close": btcusd.Close.values.flatten(),
        }).iloc[-1]
        # rprint(f"Time: {data.Date}  Ticker: BTCUSD  Price: {data.Close}")
        table.add_row(
            f"{data.Date}", "BTC-USD", f"[green]{data.Close}"
        )
        time.sleep(60)
        live.update(table)




