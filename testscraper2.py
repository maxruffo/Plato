import yfinance as yf
import pandas as pd

# Definieren des Tickersymbols
tickerSymbol = "AAPL"

# Abrufen der Daten
data = yf.Ticker(tickerSymbol)

# Abrufen der Finanzdaten
financials = data.financials
df_financials = pd.DataFrame(financials)

# Abrufen der Analystenbewertungen
analyst_ratings = data.recommendations
df_analyst_ratings = pd.DataFrame(analyst_ratings)

# Abrufen der historischen Preise
historical_prices = data.history(period="max")
df_historical_prices = pd.DataFrame(historical_prices)

# Abrufen der Dividendendaten
dividends = data.dividends
df_dividends = pd.DataFrame(dividends)

# Abrufen von Unternehmensdaten
company_profile = data.info
df_company_profile = pd.DataFrame(company_profile.items(), columns=["Eigenschaft", "Wert"])

# Abrufen von ESG-Kennzahlen
esg_data = data.sustainability
df_esg_data = pd.DataFrame(esg_data)

# Abrufen von Marktdaten
market_data = data.info
df_market_data = pd.DataFrame({
    "Marktkapitalisierung": [market_data["marketCap"]],
    "KGV": [market_data["forwardPE"]],
    "PEG": [market_data["pegRatio"]],
    "Buchwert pro Aktie": [market_data["bookValue"]],
    "Kurs-Gewinn-Verhältnis (P/E Ratio)": [market_data["trailingPE"]],
    "Kurs-Buchwert-Verhältnis (P/B Ratio)": [market_data["priceToBook"]],
    "Umsatzwachstum (letztes Quartal)": [market_data["revenueGrowth"]],
    "EPS-Wachstum (letztes Quartal)": [market_data["earningsGrowth"]],
    "Dividendenrendite": [market_data["dividendYield"]],
    "Beta": [market_data["beta"]],
    "Volatilität (1 Jahr)": [market_data["volatility"]],
    "52-Wochen-Hoch": [market_data["fiftyTwoWeekHigh"]],
    "52-Wochen-Tief": [market_data["fiftyTwoWeekLow"]],
    "Anzahl der ausstehenden Aktien": [market_data["sharesOutstanding"]]
})

# Abrufen von Daten zu den Wettbewerbern des Unternehmens
competitors = data.recommendations

# Erstellen des DataFrames für die Wettbewerberdaten
df_competitors = pd.DataFrame({
    "Datum": competitors.index,
    "Rating": competitors["To Grade"].values
})

# Zusammenführen der einzelnen DataFrames
df = pd.concat([df_financials, df_analyst_ratings, df_historical_prices, df_dividends,
                df_company_profile, df_esg_data, df_market_data, df_competitors], axis=1)

# Ausgabe des resultierenden DataFrames
print(df)
