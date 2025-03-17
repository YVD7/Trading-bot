# Live trade code  
import datetime, time 
import talib as ta 
import pandas as pd 
import yfinance as yf 

from logger.CustomLogger import CustomLogger


current_time = datetime.datetime.now().time()
start_time = datetime.time(9, 30)
end_time = datetime.time(15, 30)
upper_band, lower_band = 70, 30
ticker = "RELIANCE.NS"


while True:
    logger = CustomLogger(__name__).get_logger()
    current_time = datetime.datetime.now().time()
    if start_time <= current_time < end_time:
        reliance = yf.download(ticker , interval="1m", period="1D")
        data = pd.DataFrame({
                "Date": reliance.index,
                "Open": reliance["Open"].values.flatten(),
                "High": reliance["High"].values.flatten(),
                "Low": reliance["Low"].values.flatten(),
                "Close": reliance["Close"].values.flatten()
            })

        data['RSI'] = ta.RSI(data['Close'], timeperiod=14)
    
        data["Signal"] = None 
        data["Profit"] = None 

        last_action = None

        for index, row in data.iterrows():
            if row["RSI"] < lower_band and last_action != "Buy":
                data.at[index, "Signal"] = "Buy"
                last_action = "Buy"
                logger.info(f"Ticker: {ticker}, Signal: Buy, Price: {row['Close']}, RSI: {row['RSI']}")

            elif row["RSI"] > upper_band and last_action == "Buy":
                data.at[index, "Signal"] = "Sell"
                last_action = "Sell"

                profit = round(
                    data[data["Signal"] == "Sell"]["Close"].iloc[-1]
                    - data[data["Signal"] == "Buy"]["Close"].iloc[-1], 2
                )

                data.at[index, "Profit"] = profit

                logger.info(f"Ticker: {ticker}, Signal: Sell, Price: {row['Close']}, Profit: {profit}, RSI: {row['RSI']}")

            elif row["RSI"] < lower_band and last_action == "Sell":
                data.at[index, "Signal"] = "Buy"
                last_action = "Buy"
                logger.info(f"Ticker: {ticker}, Signal: Buy, Price: {row['Close']}, RSI: {row['RSI']}")

        TotalProfit = float(sum(data[data["Signal"] == "Sell"]["Profit"]))
        logger.info(f"Ticker: {ticker}, Total Profit: {TotalProfit}")
    
    else:
        logger.info("Market is closed. Waiting for next trading session.")
        break
    
    time.sleep(60)
