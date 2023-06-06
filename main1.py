import requests

url = f"https://query1.finance.yahoo.com/v7/finance/download/AAPL?period1=345427200&period2=1680566400&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content = requests.get(url, headers=headers).content
# print(content)

with open('dataone.csv', 'wb') as file:
    file.write(content)
