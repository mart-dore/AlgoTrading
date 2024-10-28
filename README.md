# AlgoTrading with the Binance API

This project is an initial exploration of algorithmic trading using the Binance API. It aims to assess the effectiveness of a trading strategy based on moving averages for the BTC/USDT pair.

## Project Overview

The goal is to test a simple buy and sell strategy using two moving averages: a short-term moving average (5-hour) and a long-term moving average (20-hour). This strategy assumes that:
- A buy signal is triggered when the 5-hour moving average crosses above the 20-hour moving average.
- A sell signal is triggered when the 5-hour moving average crosses below the 20-hour moving average.

If backtesting results are promising, this strategy could be implemented in a live trading environment.

## Files and Directories

- **get_started.ipynb**: Jupyter Notebook introducing the trading strategy, data collection, and backtesting. This serves as a first step in evaluating the strategy's potential.
- 
## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/AlgoTrading-Binance.git
   ```
2. Run `get_started.ipynb` to explore the initial strategy and backtesting results.

## Future Enhancements

- **Enhanced Indicators**: Test additional indicators such as RSI and Bollinger Bands for a more robust strategy.
- **Parameter Optimization**: Adjust and optimize the moving average windows for better performance.
- **Live Trading Execution**: If the backtesting proves effective, extend the code to execute trades in real-time on Binance.
