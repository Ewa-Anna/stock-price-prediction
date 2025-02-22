import requests
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from django.shortcuts import render


def fetch_stock_data(ticker):
    stock_data = yf.download(ticker, period="1y")

    stock_data.reset_index(inplace=True)

    historical_data = stock_data[["Date", "Close"]]
    return historical_data


def train_model(historical_data):
    historical_data["Date"] = pd.to_datetime(historical_data["Date"])
    historical_data["Date"] = historical_data["Date"].map(pd.Timestamp.timestamp)

    X = historical_data[["Date"]].values.reshape(-1, 1)
    y = historical_data["Close"].values

    model = LinearRegression().fit(X, y)
    return model


def predict_stock(request):
    ticker = None
    company_name = None
    predicted_price = None
    dates = []
    prices = []

    tickers = get_tickers()

    if request.method == "POST":
        ticker = request.POST.get("ticker").upper()

        historical_data = fetch_stock_data(ticker)

        if historical_data.empty:
            return render(
                request,
                "predictor/main.html",
                {"tickers": tickers, "error": "No data found for this ticker."},
            )

        company_name = get_full_company_name(ticker)

        dates = historical_data["Date"].dt.strftime("%Y-%m-%d").tolist()
        prices = historical_data["Close"].values.flatten().tolist()

        model = train_model(historical_data)
        future_date = np.array(
            [[pd.Timestamp.now().timestamp() + 86400]]
        )  # The next day: 86400 is 24h (24x60x60)
        predicted_price = model.predict(future_date)

        context = {
            "tickers": tickers,
            "ticker": ticker,
            "company_name": company_name,
            "dates": dates,
            "prices": prices,
            "predicted_price": predicted_price[0],
        }
        return render(request, "predictor/main.html", context)

    return render(
        request,
        "predictor/main.html",
        {
            "tickers": tickers,
        },
    )


def get_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    table = soup.find("table", {"class": "wikitable"})

    tickers = []
    for row in table.find_all("tr")[1:]:
        ticker = row.find_all("td")[0].text.strip()
        tickers.append(ticker)

    return tickers


def get_full_company_name(ticker):
    stock = yf.Ticker(ticker)
    return stock.info.get("longName", "Unknown Company")
