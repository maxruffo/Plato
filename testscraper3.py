import yfinance as yf

msft = yf.Ticker("MSFT")

# get all stock info
msft.info

# get historical market data
hist = msft.history(period="1mo")

# show meta information about the history (requires history() to be called first)
msft.history_metadata

# show actions (dividends, splits, capital gains)
msft.actions
msft.dividends
msft.splits
msft.capital_gains  # only for mutual funds & etfs

# show share count
# - yearly summary:

#FUNKTIONIERT NICHT:    msft.shares    

# - accurate time-series count:
msft.get_shares_full(start="2022-01-01", end=None)

# show financials:
# - income statement

#FUNKTIONIERT NICHT:   msft.income_stmt

#FUNKTIONIERT NICHT:   msft.quarterly_income_stmt

# - balance sheet

#FUNKTIONIERT NICHT:   msft.balance_sheet

#FUNKTIONIERT NICHT:   msft.quarterly_balance_sheet

# - cash flow statement

#FUNKTIONIERT NICHT:   msft.cashflow

#FUNKTIONIERT NICHT:   msft.quarterly_cashflow

# see `Ticker.get_income_stmt()` for more options

# show holders
msft.major_holders
msft.institutional_holders
msft.mutualfund_holders

# show earnings

#FUNKTIONIERT NICHT:   msft.earnings

#FUNKTIONIERT NICHT:   msft.quarterly_earnings

# show sustainability

#FUNKTIONIERT NICHT:   msft.sustainability

# show analysts recommendations

#FUNKTIONIERT NICHT:   msft.recommendations

#FUNKTIONIERT NICHT:   msft.recommendations_summary


# show analysts other work

#FUNKTIONIERT NICHT:   msft.analyst_price_target

#FUNKTIONIERT NICHT:   msft.revenue_forecasts

#FUNKTIONIERT NICHT:   msft.earnings_forecasts

#FUNKTIONIERT NICHT:   msft.earnings_trend

# show next event (earnings, etc)
#FUNKTIONIERT NICHT:   msft.calendar

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
msft.earnings_dates

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
msft.isin

# show options expirations

msft.options

# show news
msft.news

print(msft.news)