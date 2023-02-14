import requests

def handle_response(message) -> str:
        p_message = message.lower()

        if p_message == 'eth':
            url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return response

        if p_message == 'btc':
            url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
            headers = {'X-CoinAPI-Key': 'A8F6F8C0-60E3-47DA-9951-3D2C91953C57'}
            response = requests.get(url, headers = headers).json()
            return response
