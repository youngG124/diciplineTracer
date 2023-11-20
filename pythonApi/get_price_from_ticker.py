import requests
from bs4 import BeautifulSoup

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
)

@app.get("/prices/{ticker_list}")
def get_prices(ticker_list: str):
    return {"price_list": get_price_from_ticker(ticker_list)}
# 일단 모든 티커 다 받아와 업데이트는 진행,
# 일정 금액 이상만 파이차트에 표시, 나머지는 기타 소형주식의 합으로 표시


def get_price_from_ticker(ticker_list_arg) :

    ticker_list = ticker_list_arg.split(',')

    price_list = []

    for i in ticker_list :
        URL = 'https://www.google.com/finance/quote/' + i + ':NASDAQ'
        Request = requests.get(URL)

        price = BeautifulSoup(Request.text, 'html.parser').find('div', class_='YMlKec fxKbKc').get_text().strip()

        price_list.append(price)

    return price_list