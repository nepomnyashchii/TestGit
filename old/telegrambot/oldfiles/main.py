from tokens import cmc_token
import requests
import json
from flask import Flask, request, Response

token = "873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM"

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        write_json(msg, 'telegram_request.json')
        return(Response('ok', status =200))
    else:
        return '<h1>CoinMarketCap bot>/h1>'

def write_json(data, filename = 'response.json'):
    with open (filename, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_cmc_data (crypto):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    # ?slug=gdax&convert=LTC,XRP,EUR
    params = {'symbol': crypto, 'convert': "USD"}
    headers = {"X-CMC_PRO_API_KEY" : cmc_token}
    r = requests.get(url, headers=headers, params=params).json()
    price = r['data'][crypto]["quote"]["USD"]["price"]
    # print(r)
    # write_json(r)
    return price


def main():
    # get_cmc_data("BTC")
    print(get_cmc_data("BTC"))

    # https://api.telegram.org/bot873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM/getMe

    # {"ok":true,"result":{"id":873802609,"is_bot":true,"first_name":"Alec","username":"nepomnyashchiiBot"}}

    # https://api.telegram.org/bot873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM/getUpdates
#    {"ok":true,"result":[{"update_id":462152619,
# "message":{"message_id":192,"from":{"id":872535835,"is_bot":false,"first_name":"Alexander","last_name":"Nepomnyashchii","language_code":"en"},"chat":{"id":872535835,"first_name":"Alexander","last_name":"Nepomnyashchii","type":"private"},"date":1562116387,"text":"Hello news"}}]}
 # https://api.telegram.org/bot873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM/sendMessage?chat_id=872535835&text=Hello news
#  {"ok":true,"result":{"message_id":193,"from":{"id":873802609,"is_bot":true,"first_name":"Alec","username":"nepomnyashchiiBot"},"chat":{"id":872535835,"first_name":"Alexander","last_name":"Nepomnyashchii","type":"private"},"date":1562117709,"text":"Hello news"}}

#answer back from the telegram


# https://api.telegram.org/bot873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM/setWebhook?url=https://rutum.serveo.net
# https://api.telegram.org/bot873802609:AAGrF4tID-CD4lufzgMjqNEnqLxhCaEweLM/deleteWebhook?url=https://rutum.serveo.net




if __name__ =='__main__':
    main()


if __name__ =='__main__':
    app.run(debug=True)


