from data_stock import DataStock
import os
from twilio.rest import Client
from data import NewsApiClient

account_sid_stock = os.environ.get("ACCOUNT_SID_ST")
auth_token_stock = os.environ.get("AUTH_TOKEN_ST")
phone_num_to = os.environ.get("PHONE_NUM_TO")
phone_num_from = os.environ.get("PHONE_NUM_FROM")

stock_data = DataStock()

latest_day = stock_data.find_stock_days()[0]
previous_day = stock_data.find_stock_days()[1]
last_day_stock = float(stock_data.data['Time Series (Daily)'][latest_day]['4. close'])
pre_day_stock = float(stock_data.data['Time Series (Daily)'][previous_day]['4. close'])
print(last_day_stock)
print(pre_day_stock)
variance = ((last_day_stock - pre_day_stock)/pre_day_stock)
percentage = ('{:,.2%}'.format(variance))

if "-" not in percentage:
    text = f"🔺{percentage}"
else:
    text = f"🔻 {percentage}"

news = NewsApiClient()
print(news.n_data)
header = news.get_articles()[0]

brief = news.get_articles()[1]
brief = brief.rstrip("[+4666 chars]")

n_url = news.get_articles()[2]

body = f"TSLA {text}\nHeadline: {header}\nBrief: {brief}\n Link: {n_url}"
print(body)
client = Client(account_sid_stock, auth_token_stock)

message = client.messages.create(
    body=f"TSLA {text}\nHeadline: {header}\nBrief: {brief}\nLink: {n_url}",
    from_=phone_num_from,
    to=phone_num_to
)

print(message.status)