"""
sp500_plot.py
Download and plot S&P 500 adjusted close prices from 2010 to 2025.

This script fetches daily S&P 500 data (^GSPC) using the yfinance library and
creates a line plot with matplotlib to visualize price trends over ~27 years.
Useful for analyzing market performance, volatility, and investment decisions.

Dependencies:
- yfinance:   For fetching market data
- pandas:     For data handling
- matplotlib: For plotting

Usage:
    python sp500_hirez_chart_2010+.py

Output:
    A matplotlib line plot showing S&P 500 adjusted close prices (1997–2025).

Author: Babar Baig
Date: April 2025
"""

import yfinance as yf
import pandas   as pd
import matplotlib.pyplot as plt

sp500 = yf.download("^GSPC", start="1997-01-01", end="2025-04-18")
# print(sp500)              # Diagnostic printout
data=sp500["Close"]         # Select column to plot

# Create a line plot
plt.figure(figsize=(20, 12))
plt.plot(data.index, data, linewidth=0.5, color="blue")
# Add labels and title
plt.title("S&P 500 Index: 2010-2025", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Adjusted Close Price", fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
#
