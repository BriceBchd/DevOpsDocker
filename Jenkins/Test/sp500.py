import yfinance as yf

sp500 = yf.Ticker('^GSPC')
sp500_hist = sp500.history(period='1d')
sp500_hist.to_csv('sp500_1d.csv')