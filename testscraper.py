import yfinance as yf
import pandas as pd

# Symbol des Unternehmens, das analysiert werden soll
symbol = "AAPL"

# Laden der Finanzdaten für das ausgewählte Unternehmen
data = yf.Ticker(symbol)

# Abrufen der Finanzkennzahlen des Unternehmens
financials = data.financials

# Erstellen des DataFrames für die Finanzkennzahlen
df_financials = pd.DataFrame({
    "Gewinn": financials.loc["Net Income"].values,
    "Umsatz": financials.loc["Total Revenue"].values,
    "Eigenkapital": financials.loc["Total Equity"].values,
    "EBITDA": financials.loc["EBITDA"].values,
    "Free Cashflow": financials.loc["Free Cash Flow"].values
})

# Abrufen der Analystenbewertungen des Unternehmens
analyst_ratings = data.recommendations

# Erstellen des DataFrames für die Analystenbewertungen
df_analyst_ratings = pd.DataFrame({
    "Datum": analyst_ratings.index,
    "Rating": analyst_ratings["To Grade"].values
})

# Abrufen der historischen Preise des Unternehmens
historical_prices = data.history(period="max")

# Erstellen des DataFrames für die historischen Preise
df_historical_prices = pd.DataFrame({
    "Datum": historical_prices.index,
    "Preis": historical_prices["Close"].values
})

# Abrufen der Dividendenzahlungen des Unternehmens
dividends = data.dividends

# Erstellen des DataFrames für die Dividendenzahlungen
df_dividends = pd.DataFrame({
    "Datum": dividends.index,
    "Dividende": dividends.values
})

# Abrufen des Unternehmensprofils
company_profile = data.info

# Erstellen des DataFrames für das Unternehmensprofil
df_company_profile = pd.DataFrame({
    "Name": [company_profile["longName"]],
    "Beschreibung": [company_profile["longBusinessSummary"]],
    "Land": [company_profile["country"]],
    "Branche": [company_profile["industry"]],
    "Mitarbeiter": [company_profile["fullTimeEmployees"]]
})

# Abrufen der ESG-Kennzahlen des Unternehmens
esg_data = data.sustainability

# Erstellen des DataFrames für die ESG-Kennzahlen
df_esg_data = pd.DataFrame({
    "Umweltbewertung": [esg_data["Value"][0]],
    "Soziale Bewertung": [esg_data["Value"][1]],
    "Governance-Bewertung": [esg_data["Value"][2]],
    "Umweltnote": [esg_data["Score"][0]],
    "Soziale Note": [esg_data["Score"][1]],
    "Governance-Note": [esg_data["Score"][2]],
})

# Abrufen der Marktdaten des Unternehmens
market_data = data.info

# Erstellen des DataFrames für die Marktdaten
df_market_data = pd.DataFrame({
    "Marktkapitalisierung": [market_data["marketCap"]],
    "KGV": [market_data["forwardPE"]],
    "PEG": [market_data["pegRatio"]],
    "Buchwert pro Aktie": [market_data["bookValue"]],
    "Kurs-Gewinn-Verhältnis (P/E Ratio)": [market_data["trailingPE"]],
    "Kurs-Buchwert-Verhältnis (P/B Ratio)": [market_data["priceToBook"]],
    "Umsatzwachstum (letztes Quartal)": [market_data["earningsQuarterlyGrowth"]],
    "EPS-Wachstum (letztes Quartal)": [market_data["quarterlyEarningsGrowthYOY"]],
    "Dividendenrendite": [market_data["dividendYield"]],
    "Beta": [market_data["beta"]],
    "Volatilität (1 Jahr)": [market_data["volatility12M"]],
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

